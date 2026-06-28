from pydantic import BaseModel, EmailStr, Field
from pydantic import ConfigDict
from uuid import UUID
from datetime import datetime


class UserCreate(BaseModel):
    username: str = Field(min_length=5, max_length=20)
    email: EmailStr
    password: str = Field(min_length=8)


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID

    username: str

    email: EmailStr

    created_at: datetime
