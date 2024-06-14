from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):

    id: int
    name: str = Field(max_length=15)
    surname: str = Field(max_length=15)
    email: str = Field(max_length=30)
    phone: str = Field(max_length=15)
    birthday: datetime
    additional_info: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True


class UpdateContact(BaseModel):

    name: Optional[str] = Field(None, max_length=15)
    surname: Optional[str] = Field(None, max_length=15)
    email: Optional[str] = Field(None, max_length=30)
    phone: Optional[str] = Field(None, max_length=15)
    birthday: Optional[datetime] = None
    additional_info: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=10)


class UserDb(BaseModel):
    id: int
    username: str
    email: str
    avatar: str

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RequestEmail(BaseModel):
    email: EmailStr
