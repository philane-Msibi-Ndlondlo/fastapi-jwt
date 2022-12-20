from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from .models.user import userModel

from .core.configs.config import settings

from .router import root_router

app = FastAPI(
    title=settings.PROJECT_NAME
)

@app.on_event("startup")
async def app_init():
    """
    Initialize crucial application services
    """
    
    db_client = AsyncIOMotorClient(settings.DATABASE_URL).xyzcompany
    
    await init_beanie(
        database=db_client,
        document_models=[
            userModel
        ]
    )

app.include_router(root_router)