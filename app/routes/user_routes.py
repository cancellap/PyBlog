from fastapi import APIRouter, Depends, HTTPException
from app.core.db import get_db
from sqlalchemy.orm import Session
from app.dtos.user_create_dto import UserCreateDTO
from app.dtos.user_response_dto import UserResponseDTO
from app.services.user_service import create_user

router = APIRouter()

@router.post("/signup", response_model=UserResponseDTO)
def create_user_endpoint(user_data: UserCreateDTO, db: Session = Depends(get_db)):
    user = create_user(db, user_data)
    return user