from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Shive"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    ALLOWED_HOSTS: List[str] = ["*"]

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 5  # 5 minutes
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7  # 7 days

    DATABASE_URL: str = "postgresql://shive:shive@localhost:5432/shive"

    class Config:
        env_file = ".env"


settings = Settings()
