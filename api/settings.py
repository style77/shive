from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Shive"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    DATABASE_URL: str = "postgresql://shive:shive@localhost:5432/shive"

    class Config:
        env_file = ".env"


settings = Settings()
