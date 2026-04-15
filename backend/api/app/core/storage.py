import os
from urllib.parse import urlparse
from uuid import uuid4

import boto3
from botocore.config import Config as BotoConfig
from botocore.exceptions import ClientError
from minio import Minio

from app.core.config import settings


class StorageClient:
    """Unified storage client for local/MinIO/S3."""

    def __init__(self) -> None:
        self.backend = self._detect_backend()
        self._minio: Minio | None = None
        self._s3 = None

    def _detect_backend(self) -> str:
        if settings.s3_endpoint:
            parsed = urlparse(settings.s3_endpoint)
            host = parsed.hostname or ""
            if "minio" in host.lower() or settings.s3_endpoint.startswith("http://minio"):
                return "minio"
            return "s3"
        return "local"

    def _get_minio(self) -> Minio:
        if self._minio is None:
            self._minio = Minio(
                urlparse(settings.s3_endpoint).netloc,
                access_key=settings.s3_access_key,
                secret_key=settings.s3_secret_key,
                secure=settings.s3_use_ssl,
            )
        return self._minio

    def _get_s3(self):
        if self._s3 is None:
            self._s3 = boto3.client(
                "s3",
                endpoint_url=settings.s3_endpoint or None,
                aws_access_key_id=settings.s3_access_key,
                aws_secret_access_key=settings.s3_secret_key,
                region_name=settings.s3_region or None,
                config=BotoConfig(signature_version="s3v4"),
            )
        return self._s3

    def upload_file(self, file_data: bytes, filename: str | None = None) -> str:
        object_name = filename or f"{uuid4().hex}"
        bucket = settings.s3_bucket or "navima"

        if self.backend == "minio":
            client = self._get_minio()
            if not client.bucket_exists(bucket):
                client.make_bucket(bucket)
            client.put_object(bucket, object_name, file_data, len(file_data))
            return object_name

        if self.backend == "s3":
            client = self._get_s3()
            client.put_object(Bucket=bucket, Key=object_name, Body=file_data)
            return object_name

        # local
        local_dir = "/tmp/navima-uploads"
        os.makedirs(local_dir, exist_ok=True)
        path = os.path.join(local_dir, object_name)
        with open(path, "wb") as f:
            f.write(file_data)
        return path

    def generate_presigned_url(self, object_name: str, expires: int = 3600) -> str:
        bucket = settings.s3_bucket or "navima"

        if self.backend == "minio":
            client = self._get_minio()
            return client.presigned_get_object(bucket, object_name, expires=expires)

        if self.backend == "s3":
            client = self._get_s3()
            try:
                return client.generate_presigned_url(
                    "get_object",
                    Params={"Bucket": bucket, "Key": object_name},
                    ExpiresIn=expires,
                )
            except ClientError:
                return ""

        # local
        return f"file://{object_name}"
