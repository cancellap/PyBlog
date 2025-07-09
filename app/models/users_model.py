from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, String
from app.models.post_model import Base 
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    deleted_at = Column(DateTime, nullable=True)
    
    posts = relationship("Post", back_populates="owner", cascade="all, delete-orphan")