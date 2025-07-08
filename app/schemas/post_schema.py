import datetime
from pydantic import BaseModel

class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    created_at: datetime
    deleted_at: datetime | None = None

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True