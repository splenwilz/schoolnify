from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .users import get_current_user, check_role
from .. import schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/schools", response_model=schemas.SchoolResponse)
def create_school(school: schemas.SchoolCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user), is_admin: bool = Depends(check_role("Admin"))):
    db_school = models.School(**school.dict())
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school
