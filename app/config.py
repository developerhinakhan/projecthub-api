from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ProjectHub-API"
    environment: str = "development"
    database_url: str
    secret_key: str
    token_expire_minutes: int = 60

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
