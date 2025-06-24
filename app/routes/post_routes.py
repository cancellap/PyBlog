from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.services.post_service import create_post
from app.core.db import get_db

router = APIRouter()
class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int


@router.post("/posts")
def create_post_route(post: PostCreate, db: Session = Depends(get_db)):
    new_post = create_post(db, post.title, post.content, post.user_id)
    return new_post