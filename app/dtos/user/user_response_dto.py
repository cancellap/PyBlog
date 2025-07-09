from pydantic import BaseModel, EmailStr

class UserResponseDTO(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True