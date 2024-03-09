from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Shive"
    secret_key: str
    algorithm: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()
