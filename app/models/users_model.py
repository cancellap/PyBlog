from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, String
from app.models.post_model import Base 
from sqlalchemy.orm import relationship
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    deleted_at = Column(DateTime, nullable=True)
    is_active = Column(Integer, default=1, nullable=False)  # 1=True, 0=False
    
    posts = relationship("Post", back_populates="owner", cascade="all, delete-orphan")
    
    def verify_password(self, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, self.password)