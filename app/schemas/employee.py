from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import date
from app.models.employee import Gender

# 共享属性
class EmployeeBase(BaseModel):
    employee_id: str
    name: str
    gender: Gender
    birth_date: date
    id_card: str
    phone: str
    email: EmailStr
    address: Optional[str] = None
    department_id: int
    position: str
    hire_date: date
    status: bool = True

# 创建时需要的属性
class EmployeeCreate(EmployeeBase):
    pass

# 更新时可以更新的属性
class EmployeeUpdate(EmployeeBase):
    employee_id: Optional[str] = None
    name: Optional[str] = None
    gender: Optional[Gender] = None
    birth_date: Optional[date] = None
    id_card: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    department_id: Optional[int] = None
    position: Optional[str] = None
    hire_date: Optional[date] = None
    status: Optional[bool] = None

# API返回的属性
class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True 