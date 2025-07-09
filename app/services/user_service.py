from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.dtos.post.post_with_user_dto import PostWithUserDTO
from app.dtos.user.user_response_dto import UserResponseDTO
from app.models.post_model import Post
from app.models.users_model import User
from app.dtos.user.user_create_dto import UserCreateDTO
from fastapi import HTTPException
from passlib.hash import bcrypt

from app.schemas.user_schema import UserSchema

def create_user(db: Session, user_data: UserCreateDTO)-> UserResponseDTO:
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
        created_at=datetime.datetime.now(timezone.utc),
        posts=[]
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(db: Session, user_id: int)-> UserResponseDTO:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return user


def get_all_posts_by_user_id_include_deleted(db: Session, user_id: int) -> PostWithUserDTO:
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    posts = db.query(Post).filter(Post.user_id == user_id).all()

    posts_with_user = PostWithUserDTO(
        id=user.id,
        user=user,
        posts=posts
    )
    return posts_with_user

def get_all_posts_by_user_id(db: Session, user_id: int) -> PostWithUserDTO:
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    posts = db.query(Post).filter(Post.user_id == user_id, Post.deleted_at == None).all()

    posts_with_user = PostWithUserDTO(
        id=user.id,
        user=user,
        posts=posts
    )

    return posts_with_user

def delete_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    user.deleted_at = datetime.now(timezone.utc)
    db.commit()
    
    return True