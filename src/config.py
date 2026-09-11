from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
    )

    TAVILY_API_KEY: str
    OPEN_ROUTER_BASE_URL: str
    OPEN_ROUTER_API_KEY: str
    OPEN_ROUTER_MODEL: str


settings = Settings()
