from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum

class Gender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String(50), unique=True, index=True)
    name = Column(String(100))
    gender = Column(Enum(Gender))
    birth_date = Column(Date)
    id_card = Column(String(18), unique=True)
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(String(200))
    department_id = Column(Integer, ForeignKey("departments.id"))
    position = Column(String(100))
    hire_date = Column(Date)
    status = Column(Boolean, default=True)  # True: 在职, False: 离职
    
    # 关系
    department = relationship("Department", back_populates="employees", foreign_keys=[department_id])
    attendance_records = relationship("Attendance", back_populates="employee")
    performance_records = relationship("Performance", back_populates="employee", foreign_keys="Performance.employee_id") 