from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.models.users_model import User
from app.services.login_service import login_user

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str
    
@router.post("")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    access_token = login_user(request.email, request.password, db)
    return {"access_token": access_token}