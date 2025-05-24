from typing import Optional
from pydantic import BaseModel, EmailStr

# 共享属性
class UserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    employee_id: Optional[int] = None

# 创建时需要的属性
class UserCreate(UserBase):
    username: str
    email: EmailStr
    password: str

# 更新时可以更新的属性
class UserUpdate(UserBase):
    password: Optional[str] = None

# API返回的属性
class User(UserBase):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

# Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: Optional[int] = None 