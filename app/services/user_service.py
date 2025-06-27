from datetime import datetime
from sqlalchemy.orm import Session
from app.models.users_model import User
from app.dtos.user_create_dto import UserCreateDTO
from fastapi import HTTPException
from passlib.hash import bcrypt

def create_user(db: Session, user_data: UserCreateDTO):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    existing_username = db.query(User).filter(User.username == user_data.username).first()
    if existing_username:
        raise HTTPException(status_code=400, detail="Username já cadastrado")
    
    hashed_password = bcrypt.hash(user_data.password)
    
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password=hashed_password,
        created_at=datetime.utcnow(),
        posts=[]
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user