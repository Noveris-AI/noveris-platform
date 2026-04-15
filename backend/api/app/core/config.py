from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # App
    app_env: str = "development"
    app_domain: str = "localhost"
    admin_domain: str = "localhost"
    enable_api_docs: bool = True

    # Database
    db_url: str = "postgresql+asyncpg://navima:navima@localhost:5432/navima"
    db_pool_size: int = 10
    db_max_overflow: int = 20
    db_pool_timeout: float = 30.0

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # Security
    secret_key: str = "change-me-in-production"
    session_timeout_seconds: int = 43200
    session_cookie_name: str = "session_id"
    session_cookie_secure: bool = False
    session_cookie_samesite: str = "lax"
    session_redis_prefix: str = "navima:session:"
    csrf_secret: str = "change-me-in-production"

    # Rate limit
    rate_limit_redis_prefix: str = "navima:rate:"

    # CORS
    cors_origins: str = "http://localhost:5173,http://localhost:5174"

    # Forward proxy
    forward_connect_timeout: float = 5.0
    forward_read_timeout: float = 60.0
    forward_max_request_size: int = 104_857_600

    # SMTP
    smtp_host: str = ""
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_password: str = ""
    smtp_tls: bool = True
    smtp_from: str = "noreply@noveris.ai"

    # License
    license_server_url: str = ""

    # Branding
    default_brand_name: str = "Navima"
    default_logo_url: str = ""

    # HuggingFace
    hf_endpoint: str = "https://huggingface.co"
    hf_api_token: str = ""

    # Object Storage
    s3_endpoint: str = ""
    s3_access_key: str = ""
    s3_secret_key: str = ""
    s3_bucket: str = ""
    s3_region: str = ""
    s3_use_ssl: bool = True

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings()
