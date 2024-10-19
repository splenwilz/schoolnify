from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .users import get_current_user, check_role
from .. import models, schemas, crud
from ..database import get_db

router = APIRouter()

@router.put("/users/{user_id}/role", response_model=schemas.UserResponse)
def assign_role(user_id: str, role_id: str, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user), is_superadmin: bool = Depends(check_role("superadmin"))):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    role = db.query(models.Role).filter(models.Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    user.role_id = role.id
    db.commit()
    db.refresh(user)

    return user
