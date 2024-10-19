from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database import SessionLocal, engine
from .models import Base
from .routes import auth, users, superadmin    
from .seed import seed_roles

Base.metadata.create_all(bind=engine)

# Define the lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    try:
        # Seed roles when the app starts
        seed_roles(db)
        yield
    finally:
        db.close()

app = FastAPI(lifespan=lifespan)

# Include routes
app.include_router(auth.router, prefix="/api/auth")
app.include_router(users.router, prefix="/api")
app.include_router(superadmin.router, prefix="/api/superadmin")
# app.include_router(schools.router, prefix="/api/schools")
