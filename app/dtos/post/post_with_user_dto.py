# DTO
from datetime import datetime

from pydantic import BaseModel

from app.schemas.post_schema import PostSchema
from app.schemas.user_schema import UserSchema

class PostWithUserDTO(BaseModel):
    id: int
    user: UserSchema    
    posts: list[PostSchema]

    class Config:
        from_attributes = True
