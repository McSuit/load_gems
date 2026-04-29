"""Настройки приложения, загружаемые из .env через pydantic-settings."""
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

_ENV_FILE = Path(__file__).parent.parent / ".env"


class Settings(BaseSettings):
    """Глобальные настройки проекта. Любое поле можно переопределить через переменную окружения или .env."""

    model_config = SettingsConfigDict(
        env_file=str(_ENV_FILE),
        env_file_encoding="utf-8",
    )

    auth_token: SecretStr
    """Bearer-токен для авторизации в API."""

    base_url: str
    """Базовый URL целевого сервиса. Задаётся через переменную BASE_URL в .env."""


settings = Settings()
