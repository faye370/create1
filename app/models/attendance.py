from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum
from datetime import datetime

class AttendanceType(str, enum.Enum):
    CHECK_IN = "check_in"
    CHECK_OUT = "check_out"
    LEAVE = "leave"
    OVERTIME = "overtime"

class AttendanceStatus(str, enum.Enum):
    NORMAL = "normal"
    LATE = "late"
    EARLY = "early"
    ABSENT = "absent"
    APPROVED = "approved"
    PENDING = "pending"
    REJECTED = "rejected"

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    date = Column(DateTime, default=datetime.utcnow)
    type = Column(Enum(AttendanceType))
    status = Column(Enum(AttendanceStatus), default=AttendanceStatus.PENDING)
    check_in_time = Column(DateTime, nullable=True)
    check_out_time = Column(DateTime, nullable=True)
    location = Column(String(200), nullable=True)  # GPS位置
    remark = Column(String(500), nullable=True)
    
    # 关系
    employee = relationship("Employee", back_populates="attendance_records") 