import os
import secrets
import json
from typing import List, Optional, Dict, Any, Union

from pydantic import AnyHttpUrl, PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Contract Management System"
    PROJECT_DESCRIPTION: str = (
        "A comprehensive contract management system with advanced features"
    )
    PROJECT_VERSION: str = "0.1.0"

    # Security settings
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    ALGORITHM: str = "HS256"

    # CORS settings
    CORS_ORIGINS: List[str] = []

    @field_validator("CORS_ORIGINS", mode="before")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str):
            try:
                # Try to parse as JSON
                return json.loads(v)
            except json.JSONDecodeError:
                # If not JSON, treat as comma-separated
                if not v.startswith("["):
                    return [i.strip() for i in v.split(",")]
        return v if isinstance(v, list) else []

    # Database settings
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "contract_management"
    POSTGRES_PORT: str = "5432"
    DATABASE_URI: Optional[PostgresDsn] = None

    @field_validator("DATABASE_URI", mode="before")
    def assemble_db_connection(cls, v: Optional[str], info) -> Any:
        if isinstance(v, str):
            return v

        # Get values from the model data
        postgres_user = info.data.get("POSTGRES_USER", "postgres")
        postgres_password = info.data.get("POSTGRES_PASSWORD", "postgres")
        postgres_server = info.data.get("POSTGRES_SERVER", "localhost")
        postgres_port = info.data.get("POSTGRES_PORT", "5432")
        postgres_db = info.data.get("POSTGRES_DB", "contract_management")

        # Convert port to integer
        try:
            port_int = int(postgres_port)
        except (ValueError, TypeError):
            port_int = 5432  # Default PostgreSQL port

        return PostgresDsn.build(
            scheme="postgresql",
            username=postgres_user,
            password=postgres_password,
            host=postgres_server,
            port=port_int,  # Use integer port
            path=f"{postgres_db}",
        )

    # Redis settings
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: Optional[str] = None

    # Celery settings
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"

    # Email settings
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = 587
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[str] = None
    EMAILS_FROM_NAME: Optional[str] = None

    # File storage settings
    STORAGE_TYPE: str = "local"  # local, s3, etc.
    S3_BUCKET_NAME: Optional[str] = None
    S3_ACCESS_KEY: Optional[str] = None
    S3_SECRET_KEY: Optional[str] = None
    S3_REGION: Optional[str] = None
    LOCAL_STORAGE_PATH: str = "app/static/uploads"

    # Superuser settings
    FIRST_SUPERUSER: str = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin"

    # Environment settings
    ENVIRONMENT: str = "development"  # development, staging, production

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


settings = Settings()
