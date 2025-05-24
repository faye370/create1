from typing import Optional
from pydantic import BaseModel

class LeaveBase(BaseModel):
    employee_id: int
    start_date: str
    end_date: str
    leave_type: str
    reason: Optional[str] = None
    status: str = "pending"

class LeaveCreate(LeaveBase):
    pass

class LeaveUpdate(LeaveBase):
    pass

class Leave(LeaveBase):
    id: int

    class Config:
        from_attributes = True 