from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class UserResponse(BaseModel):
    name: Optional[str]
    email: str
    phone: Optional[str]
    address: Optional[str]
    is_active: bool
    created_at: datetime

class UserListRepoonse(BaseModel):
    result: List[UserResponse]