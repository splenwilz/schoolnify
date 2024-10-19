from sqlalchemy.orm import Session
from .models import Role
import uuid

def seed_roles(db: Session):
    roles = [
        {"id": uuid.uuid4(), "name": "superadmin", "description": "Super Admin Role"},
        {"id": uuid.uuid4(), "name": "admin", "description": "Admin Role"},
        {"id": uuid.uuid4(), "name": "teacher", "description": "Teacher Role"},
        {"id": uuid.uuid4(), "name": "student", "description": "Student Role"},
    ]

    for role_data in roles:
        role = db.query(Role).filter(Role.name == role_data["name"]).first()
        if not role:
            new_role = Role(id=role_data["id"], name=role_data["name"], description=role_data["description"])
            db.add(new_role)
    
    db.commit()
