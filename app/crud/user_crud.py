from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user_schema import UserCreate

def create_user_db(db: Session, user_in: UserCreate):
    user = User(name=user_in.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users_db(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()
