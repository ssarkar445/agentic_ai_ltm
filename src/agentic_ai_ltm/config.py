from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # API keys
    groq_api_key: SecretStr
    openai_api_key: SecretStr
    tavily_api_key: SecretStr
    langsmith_api_key: SecretStr

    # LangSmith
    langsmith_tracing: bool = False
    langsmith_project: str = "agent-longterm_memory"

    # Database
    supabase_database_url: SecretStr

    # Application
    app_env: Literal["development", "staging", "production"] = "development"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"

    # Reliability / performance
    rate_limit: int = 60
    cache_ttl_seconds: int = 300
    max_retries: int = 3


settings = Settings()