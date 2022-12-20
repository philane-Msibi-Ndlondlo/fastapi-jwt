from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.get("/register")
async def register_user():
    return {"message": "Register Path"} 