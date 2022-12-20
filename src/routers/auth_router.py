from fastapi import APIRouter, status, HTTPException

from datetime import datetime

from ..schemas.user_schema import UserRegisterSchema, UserRegisterResponseSchema

from ..models.user import userModel

from ..utils.password_utils import passwordUtils

auth_router = APIRouter()

@auth_router.post("/register", summary="Registers A New User", status_code=status.HTTP_201_CREATED, response_model=UserRegisterResponseSchema)
async def register_user(user: UserRegisterSchema):
    """
    Handles the resgistration of a new user

    Returns:
        _type_: _description_
    """
    
    user_exists = await userModel.by_email(user.email)
    
    if user_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User Already Exists")
        
    new_user = userModel(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        nickname=user.nickname,
        password=user.password,
        date_created= str(datetime.now())
    )
        
    try:
        await new_user.save()
        return UserRegisterResponseSchema(message="User Registered Successfully")
        
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to create user record. {exc}")
        