from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from .. import schemas, models, crud
from ..database import get_db
from ..utils.security import hash_password, verify_password, authenticate_user
from ..utils.jwt import create_jwt_token

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

@router.post("/register", response_model=schemas.TokenResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    if not user.role_id:
        student_role = db.query(models.Role).filter(models.Role.name == "student").first()
        if not student_role:
            raise HTTPException(status_code=500, detail="Student role not found. Contact admin.")
        user.role_id = student_role.id

    # Hash the password
    original_password = user.password
    user.password = hash_password(original_password)

    # Create the user
    new_user = crud.create_user(db=db, user=user)

    # Verify the password after user creation (optional step)
    if not verify_password(original_password, new_user.password):
        db.rollback()
        raise HTTPException(status_code=500, detail="Error during user creation")

    # Generate JWT token
    access_token = create_jwt_token(user=new_user, db=db)
    user_response = schemas.UserResponse.model_validate(new_user)
    return {"access_token": access_token, "token_type": "bearer", "user": user_response}



@router.post("/login", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    access_token = create_jwt_token(user=user, db=db)
    return {"access_token": access_token, "token_type": "bearer"}