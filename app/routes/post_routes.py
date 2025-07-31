from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.services.post_service import create_post, get_post_by_id, delete_post_by_id, get_all_posts_include_deleted, get_all_posts
from app.core.db import get_db
from app.utils.auth import get_current_user

router = APIRouter()
class PostCreate(BaseModel):
    title: str
    content: str

@router.post("/publish")
def create_post_route(post: PostCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    new_post = create_post(db, post.title, post.content, current_user.id)
    return new_post
 
@router.get("/getsPosts/includeDeleted")
def get_all_posts_include_deleted_endpoint(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    posts = get_all_posts_include_deleted(db)
    return posts

@router.get("/getPosts")
def get_all_posts_endpoint(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    posts = get_all_posts(db)
    return posts

@router.get("/getPost/{post_id}")
def get_post_route(post_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    post = get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.delete("/{post_id}")
def delete_post_route(post_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    post = delete_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
