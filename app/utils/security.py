from passlib.context import CryptContext
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models

# Initialize password context with Argon2
pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    """Hashes a password using Argon2."""
    password = password.strip()
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a password against a stored hash."""
    return pwd_context.verify(plain_password.strip(), hashed_password.strip())

def authenticate_user(db: Session, email: str, password: str):
    """Authenticate user by verifying credentials."""
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    return user
