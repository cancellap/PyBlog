from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.post_service import create_post
from app.core.db import get_db

router = APIRouter()

@router.post("/posts")
def create_post_route(title: str, content: str, user_id: int, db: Session = Depends(get_db)):
    post = create_post(db, title, content, user_id)
    return post