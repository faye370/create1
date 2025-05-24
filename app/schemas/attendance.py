from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from app.models.attendance import AttendanceType, AttendanceStatus

# 共享属性
class AttendanceBase(BaseModel):
    type: AttendanceType
    status: AttendanceStatus = AttendanceStatus.PENDING
    check_in_time: Optional[datetime] = None
    check_out_time: Optional[datetime] = None
    location: Optional[str] = None
    remark: Optional[str] = None

# 创建时需要的属性
class AttendanceCreate(AttendanceBase):
    pass

# 请假申请
class LeaveCreate(BaseModel):
    start_time: datetime
    end_time: datetime
    type: AttendanceType = AttendanceType.LEAVE
    remark: str

# 更新时可以更新的属性
class AttendanceUpdate(AttendanceBase):
    type: Optional[AttendanceType] = None
    status: Optional[AttendanceStatus] = None
    check_in_time: Optional[datetime] = None
    check_out_time: Optional[datetime] = None
    location: Optional[str] = None
    remark: Optional[str] = None

# API返回的属性
class Attendance(AttendanceBase):
    id: int
    employee_id: int
    date: datetime

    class Config:
        orm_mode = True 