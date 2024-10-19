from sqlalchemy.orm import Session
from . import models, schemas
import uuid

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        id=uuid.uuid4(),
        email=user.email,
        password=user.password,
        name=user.name,
        role_id=user.role_id,  # Use role_id here
        tenant_id=user.tenant_id if user.tenant_id else None,  # Handle nullable tenant_id
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
