from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Crab Age Prediction"
    DATABASE_URL: str

    class Config:
        env_file = ".env"

setting = Settings()