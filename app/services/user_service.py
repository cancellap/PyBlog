from datetime import datetime
from sqlalchemy.orm import Session
from app.models.post_model import Post
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

def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return user


def get_all_posts_by_user_id(db: Session, user_id: int):
    posts = db.query(Post).filter(Post.user_id == user_id).all()
    post_list = []
    # for post in posts:
    #     user = db.query(User).filter(User.id == post.user_id).first()
    #     post_return = {
    #         "id": post.id,
    #         "title": post.title,
    #         "content": post.content,
    #         "created_at": post.created_at,
    #         "user_id": post.user_id,
    #         "username": user.username if user else None
    #     }
    #     post_list.append(post_return)
    return posts