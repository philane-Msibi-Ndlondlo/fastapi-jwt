from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from uuid import UUID

class UserSchema(BaseModel):
    """
    Defines the base schema of the user's request and response body

    Args:
        BaseModel
    """
    firstname: str = Field(..., description="The First Name Of The User", min_length=3, max_length=20)
    lastname: str = Field(..., description="The Last Name Of The User", min_length=3, max_length=20)
    nickname: Optional[str] = Field(default=None, description="The Nickname or Prefered Name Of The User")
    email: EmailStr = Field(...,description="The Email Address Of The User")
    password: str = Field(..., description="The Password Of The User", min_length=8, max_length=20)
    active: bool = Field(default=False, description="The Password Of The User") 
    
class UserRegisterSchema(BaseModel):
    """
    Defines the schema of the request bosy when the user is registering

    Args:
        BaseModel
    """
    firstname: str = Field(..., description="The First Name Of The User", min_length=3, max_length=20)
    lastname: str = Field(..., description="The Last Name Of The User", min_length=3, max_length=20)
    nickname: Optional[str] = Field(default=None, description="The Nickname or Prefered Name Of The User")
    email: EmailStr = Field(...,description="The Email Address Of The User")
    password: str = Field(..., description="The Password Of The User", min_length=8, max_length=20)
    
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
    message: str = Field(..., description="Message of outcome")
    
    class Config:
        schema_extra = {
            "example": {
                "message": "Message Added Succesfully"
            }
        }
        
        
        
class UserLoginSchema(BaseModel):
    """
    Defines the schema of the request body when the user is logging in

    Args:
        BaseModel
    """
    email: EmailStr = Field(...,description="The Email Address Of The User")
    password: str = Field(..., description="The Password Of The User", min_length=8, max_length=20)
    
    class Config:
        schema_extra = {
            "example": {
                "email": "jane@doe.com",
                "password": "J@n3D03!"
            }
        }
        
class UserLoginResponseSchema(BaseModel):
    """
    Schema that defines the schema of the response after the user has been logging In

    Args:
        BaseModel
    """
    message: str = Field(..., description="Message of outcome")
    
    class Config:
        schema_extra = {
            "example": {
                "message": "Message Added Succesfully"
            }
        }
        