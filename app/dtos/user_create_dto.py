from pydantic import BaseModel, EmailStr, Field, model_validator

class UserCreateDTO(BaseModel):
    email: EmailStr = Field(..., description="User email address")
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        description="Password with at least 8 characters, including letters and numbers"
    )
    confirm_password: str = Field(..., description="Password confirmation")
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Username with 3 to 50 characters"
    )

    @model_validator(mode="after")
    def validate_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        if not any(c.isalpha() for c in self.password):
            raise ValueError("Password must contain at least one letter")
        if not any(c.isdigit() for c in self.password):
            raise ValueError("Password must contain at least one number")
        return self
