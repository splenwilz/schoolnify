from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

# Schema for creating a new user
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    tenant_id: Optional[UUID] = None  # Optional tenant_id with default None
    role_id: Optional[UUID] = None    # Use UUID for role_id if it's a UUID in your DB

# Schema for returning a user response
class UserResponse(BaseModel):
    id: UUID
    email: str
    name: str
    role_id: UUID   # Use UUID here for consistency
    tenant_id: Optional[UUID] = None
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True  # Enables from_orm to map SQLAlchemy models
        # Model for the token and user response
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

# Schema for login
class LoginSchema(BaseModel):
    email: EmailStr  # Use EmailStr to ensure email format validation
    password: str

# Schema for JWT token response
class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True  # Allows from_orm when needed
