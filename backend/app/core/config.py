from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str
    PROJECT_VERSION: str
    DEBUG: bool
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()