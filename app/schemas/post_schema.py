import datetime
from pydantic import BaseModel

class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True