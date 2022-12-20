from pydantic import BaseSettings
from decouple import config

class Settings(BaseSettings):
    TITLE: str = "FastAPI with JWT Auth"
    ENVIRONMENT = config('ENVIRONMENT', cast=str)
    JWT_ACCESS_KEY = config('JWT_ACCESS_KEY', cast=str)
    JWT_REFRESH_KEY = config('JWT_REFRESH_KEY', cast=str)
    DATABASE_URL: str = config("DATABASE_URL", cast=str)
    
    class Config:
        case_sensetive: bool = True