from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    HF_TOKEN: str
    ALLOWED_ORIGINS: str = "http://localhost:3000"

    class Config:
        env_file = ".env"

settings = Settings() 