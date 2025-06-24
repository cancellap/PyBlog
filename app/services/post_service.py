from sqlalchemy.orm import Session
from app.models.post_model import Post

def create_post(db: Session, title: str, content: str, user_id: int):
    new_post = Post(title=title, content=content, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post