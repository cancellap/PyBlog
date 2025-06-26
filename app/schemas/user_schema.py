import datetime
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True