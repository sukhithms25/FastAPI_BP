from sqlalchemy.orm import Session
from app.crud.user_crud import create_user_db, get_users_db
from app.schemas.user_schema import UserCreate

def create_user(db: Session, user_in: UserCreate):
    return create_user_db(db, user_in)

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return get_users_db(db, skip=skip, limit=limit)
