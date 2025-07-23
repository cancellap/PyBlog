from fastapi import HTTPException
from app.core.db import get_db
from sqlalchemy.orm import Session
from app.models.users_model import User

from app.models.users_model import User
from app.services.jwt_service import create_access_token

def login_user(email: str, password: str, db: Session) -> str:
    user = db.query(User).filter(User.email == email).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="Not found user with this email")

    if not user.verify_password(password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = create_access_token(user.id, user.email)
    return access_token
