from typing import Optional
from pydantic import BaseModel, EmailStr, model_validator


class LoginResponse():
    access_token: str
    token_type: str

class RegisterRequest(BaseModel):
    name: Optional[str]
    email: EmailStr
    phone: Optional[int]
    address: Optional[str]
    password: str
    confirm_password: str
    @model_validator(mode="after")
    def validate_passwords(self):

        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")

        return self

class RegisterResponse(BaseModel):
    id: Optional[int]
    message: str


class TokenData(BaseModel):
    id: int = None