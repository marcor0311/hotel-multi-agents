"""Environment-backed application settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings with safe local defaults."""

    app_name: str = "Luxury Hotel AI Concierge"
    app_env: str = "development"
    log_level: str = "INFO"
    hotel_timezone: str = "America/Los_Angeles"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
