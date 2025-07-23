from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.post_model import Post
from app.models.users_model import User

def create_post(db: Session, title: str, content: str, user_id: int):
    new_post = Post(title=title, content=content, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_post_by_id(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    user = db.query(User).filter(User.id == post.user_id).first()
    post_return ={
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "created_at": post.created_at,
        "user_id": post.user_id,
        "username": user.username if user else None
    }
    return post_return

def delete_post_by_id(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.deleted_at = datetime.now(timezone.utc)
        db.commit()
        return {"detail": "Post deleted successfully"}
    else:
        return {"detail": "Post not found"}
    
def get_all_posts_include_deleted(db: Session):
    posts = db.query(Post).all()
    return posts

def get_all_posts(db: Session):
    posts = db.query(Post).filter(Post.deleted_at == None).all()
    return posts