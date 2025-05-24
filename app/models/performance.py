from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum
from datetime import datetime

class PerformanceLevel(str, enum.Enum):
    EXCELLENT = "excellent"  # 优秀
    GOOD = "good"          # 良好
    AVERAGE = "average"    # 一般
    POOR = "poor"          # 差

class Performance(Base):
    __tablename__ = "performance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    year = Column(Integer)
    month = Column(Integer)
    score = Column(Float)
    level = Column(Enum(PerformanceLevel))
    evaluation_date = Column(DateTime, default=datetime.utcnow)
    evaluator_id = Column(Integer, ForeignKey("employees.id"))
    comment = Column(String(1000))
    
    # 关系
    employee = relationship("Employee", foreign_keys=[employee_id], back_populates="performance_records")
    evaluator = relationship("Employee", foreign_keys=[evaluator_id]) 