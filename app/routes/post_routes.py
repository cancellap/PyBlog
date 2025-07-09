from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.services.post_service import create_post, get_post_by_id, delete_post_by_id,get_all_posts_include_deleted
from app.core.db import get_db

router = APIRouter()
class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int


@router.post("/publish")
def create_post_route(post: PostCreate, db: Session = Depends(get_db)):
    new_post = create_post(db, post.title, post.content, post.user_id)
    return new_post
 
@router.get("/getsPosts/includeDeleted")
def get_all_posts_include_deleted_endpoint(db: Session = Depends(get_db)): 
    posts = get_all_posts_include_deleted(db)
    return posts

@router.get("/getPost/{post_id}")
def get_post_route(post_id: int, db: Session = Depends(get_db)):
    post = get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.delete("/{post_id}")
def delete_post_route(post_id: int, db: Session = Depends(get_db)):
    post = delete_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
