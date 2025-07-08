from fastapi import APIRouter, Depends, HTTPException
from app.core.db import get_db
from sqlalchemy.orm import Session
from app.dtos.user_create_dto import UserCreateDTO
from app.dtos.user_response_dto import UserResponseDTO
from app.services.user_service import create_user, get_user_by_id, get_all_posts_by_user_id

router = APIRouter()

@router.post("/signup", response_model=UserResponseDTO)
def create_user_route(user_data: UserCreateDTO, db: Session = Depends(get_db)):
    user = create_user(db, user_data)
    return user

@router.get("/{user_id}", response_model=UserResponseDTO)
def get_user_by_id_route(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    return user

@router.get("/{user_id}/posts", response_model=list[UserResponseDTO])
def get_all_posts_by_user_id_route(user_id: int, db: Session = Depends(get_db)):
    posts = get_all_posts_by_user_id(db, user_id)
    return posts