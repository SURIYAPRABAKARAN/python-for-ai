from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    age: int
    email: str
    education: Optional[str] = None

# This is your "Wrapper" DTO
class UserResponse(BaseModel):
    message: str
    data: User