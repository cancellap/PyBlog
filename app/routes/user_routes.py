from fastapi import APIRouter, Depends, HTTPException
from app.core.db import get_db
from sqlalchemy.orm import Session
from app.dtos.post.post_with_user_dto import PostWithUserDTO
from app.dtos.user.user_create_dto import UserCreateDTO
from app.dtos.user.user_response_dto import UserResponseDTO
from app.schemas.post_schema import PostSchema
from app.services.user_service import create_user, delete_user_by_id, get_all_posts_by_user_id_include_deleted, get_user_by_id, get_all_posts_by_user_id

router = APIRouter()

@router.post("/signup", response_model=UserResponseDTO)
def create_user_route(user_data: UserCreateDTO, db: Session = Depends(get_db)):
    user = create_user(db, user_data)
    return user

@router.get("/{user_id}", response_model=UserResponseDTO)
def get_user_by_id_route(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    return user

@router.get("/{user_id}/posts/includeDeleted", response_model=PostWithUserDTO)
def get_all_posts_by_user_id_route_include_deleted(user_id: int, db: Session = Depends(get_db)):
    posts = get_all_posts_by_user_id_include_deleted(db, user_id)
    return posts

@router.get("/{user_id}/posts", response_model=PostWithUserDTO)
def get_all_posts_by_user_id_route(user_id: int, db: Session = Depends(get_db)):
    posts = get_all_posts_by_user_id(db, user_id)
    return posts

@router.delete("/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    result = delete_user_by_id(db, user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
