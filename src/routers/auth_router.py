from fastapi import APIRouter, status

from ..schemas.user_schema import UserRegisterSchema, UserRegisterResponseSchema

auth_router = APIRouter()

@auth_router.post("/register", summary="Registers A New User", status_code=status.HTTP_201_CREATED, response_model=UserRegisterResponseSchema)
async def register_user(user: UserRegisterSchema):
    """
    Handles the resgistration of a new user

    Returns:
        _type_: _description_
    """
    
    return UserRegisterResponseSchema(uuid="ab87e1c0-bc4e-44e9-9c45-e09cdb237a2f", firstname=user.firstname, lastname=user.lastname, email=user.email, date_created= "2022-12-20 16:10:58.138676")