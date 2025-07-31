from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.users_model import User
from app.services.jwt_service import create_access_token

def login_user(username: str, password: str, db: Session) -> str:
    user = db.query(User).filter(User.username == username, User.is_active == 1).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    if not user.verify_password(password):
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
    access_token = create_access_token(user.id, user.email)
    return access_token
