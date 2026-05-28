import os


def _to_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


class Settings:
    app_name: str = os.getenv("APP_NAME", "FastAPI Blog Application")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./blog.db")
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "change-this-in-production")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    refresh_token_expire_minutes: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES", "10080"))
    auto_create_tables: bool = _to_bool(os.getenv("AUTO_CREATE_TABLES"), default=False)
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
