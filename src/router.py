from fastapi import APIRouter

from .routers.auth_router import auth_router

root_router = APIRouter()

root_router.include_router(auth_router)

