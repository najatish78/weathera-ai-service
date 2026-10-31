from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Read from environment variables, or from the git-ignored `.env`."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    llm_base_url: str = "https://generativelanguage.googleapis.com/v1beta/openai/"
    llm_api_key: str = ""
    llm_model: str = "gemini-2.5-flash"

    app_api_key: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
