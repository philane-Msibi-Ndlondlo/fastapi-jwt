from pydantic import BaseSettings
from decouple import config

class Settings(BaseSettings):
    """
    This entity handles the app's constants and environment vars

    Args:
        BaseSettings
    """
    API_URL: str = "/api/v1"
    OPENAPI_URL: str = f"{API_URL}/openapi-.json"
    PROJECT_NAME: str = "FastAPI with JWT Auth"
    ENVIRONMENT = config('ENVIRONMENT', cast=str)
    JWT_ACCESS_KEY = config('JWT_ACCESS_KEY', cast=str)
    JWT_REFRESH_KEY = config('JWT_REFRESH_KEY', cast=str)
    DATABASE_URL: str = config("DATABASE_URL", cast=str)
    
    class Config:
        case_sensetive: bool = True
        
settings = Settings()