from datetime import datetime, timezone
from pydantic import BaseModel, Field, EmailStr
from uuid import uuid4, UUID
from enum import Enum

class Timestamp(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {UUID: str}

class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"

class User(Timestamp):
    email: EmailStr
    role: Role
    is_active: bool = False
