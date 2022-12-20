from fastapi import FastAPI

from .core.configs.config import settings

from .router import root_router

app = FastAPI(
    title=settings.PROJECT_NAME
)

app.include_router(root_router)