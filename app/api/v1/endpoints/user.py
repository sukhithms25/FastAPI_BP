from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.services.user_service import create_user, get_users
from app.schemas.user_schema import UserCreate, UserResponse

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user_route(user_in: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user_in)

@router.get("/", response_model=list[UserResponse])
def get_users_route(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)
