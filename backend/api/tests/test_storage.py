from app.core.config import settings
from app.core.storage import StorageClient


def test_storage_local_upload_and_presigned():
    # Force local backend by clearing endpoint
    original_endpoint = settings.s3_endpoint
    settings.s3_endpoint = ""
    settings.s3_bucket = ""

    client = StorageClient()
    assert client.backend == "local"

    content = b"hello navima"
    path = client.upload_file(content, filename="test.txt")
    assert path.endswith("test.txt")

    url = client.generate_presigned_url("test.txt")
    assert url.startswith("file://")

    settings.s3_endpoint = original_endpoint
