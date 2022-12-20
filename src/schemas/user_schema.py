from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from uuid import UUID

class UserSchema(BaseModel):
    """
    Defines the base schema of the user's request and response body

    Args:
        BaseModel
    """
    firstname: str = Field(..., description="The First Name Of The User")
    lastname: str = Field(..., description="The Last Name Of The User")
    nickname: Optional[str] = Field(default=None, description="The Nickname or Prefered Name Of The User")
    email: EmailStr = Field(..., description="The Email Address Of The User")
    password: str = Field(..., description="The Password Of The User")
    active: bool = Field(default=False, description="The Password Of The User") 
    
class UserRegisterSchema(BaseModel):
    """
    Defines the schema of the request bosy when the user is registering

    Args:
        BaseModel
    """
    firstname: str = Field(..., description="The First Name Of The User")
    lastname: str = Field(..., description="The Last Name Of The User")
    nickname: Optional[str] = Field(default=None, description="The Nickname or Prefered Name Of The User")
    email: EmailStr = Field(..., description="The Email Address Of The User")
    password: str = Field(..., description="The Password Of The User")
    
    class Config:
        schema_extra = {
            "example": {
                "firstname": "Jane",
                "lastname": "Doe",
                "nickname": "Janey",
                "email": "jane@doe.com",
                "password": "J@n3D03!"
            }
        }
        
class UserRegisterResponseSchema(BaseModel):
    """
    Schema that defines the schema of the response after the user has been registered

    Args:
        BaseModel
    """
    uuid: UUID = Field(..., description="The unique identifier of the user's record")
    firstname: str = Field(..., description="The First Name Of The User")
    lastname: str = Field(..., description="The Last Name Of The User")
    nickname: Optional[str] = Field(default=None, description="The Nickname or Prefered Name Of The User")
    email: EmailStr = Field(..., description="The Email Address Of The User")
    date_created: str = Field(default=None, description="The user's record's created timestamp")
    
    class Config:
        schema_extra = {
            "example": {
                "uuid": "ab87e1c0-bc4e-44e9-9c45-e09cdb237a2f",
                "firstname": "Jane",
                "lastname": "Doe",
                "nickname": "Janey",
                "email": "jane@doe.com",
                "date_created": "2022-12-20 16:10:58.138676"
            }
        }