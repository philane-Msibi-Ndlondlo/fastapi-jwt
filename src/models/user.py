from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import Field, EmailStr
from typing import Optional
from datetime import datetime

class userModel(Document):
    """
    Defines the User model on the database

    Args:
        Document
    """
    
    uuid: UUID = Field(default_factory=uuid4)
    firstname: str = Indexed(str)
    lastname: str = Indexed(str)
    nickname: Optional[str] = Field(default_factory=None)
    email: Indexed(EmailStr, unique=True)
    password: str
    date_created: str = datetime.now()
    active: bool = False
    
    def __repr__(self) -> str:
        return f"<User firstname='{self.firstname}' lastname='{self.lastname}' email='{self.email}' />"
    
    def __str__(self) -> str:
        return f"{self.email}"
    
    def __eq__(self, other_user: object) -> str:
        return isinstance(other_user, userModel) and other_user.email == self.email
    
    @property
    def create(self) -> datetime:
        return self.id.generation_time
    
    @classmethod
    async def by_email(self, email: str):
        return await self.find_one(self.email == email)
    
    class Collection:
        name = "users"