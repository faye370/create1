from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime
from app.models.performance import PerformanceLevel

# 共享属性
class PerformanceBase(BaseModel):
    year: int
    month: int
    score: float
    level: PerformanceLevel
    comment: str

# 创建时需要的属性
class PerformanceCreate(PerformanceBase):
    employee_id: int

# 更新时可以更新的属性
class PerformanceUpdate(PerformanceBase):
    year: Optional[int] = None
    month: Optional[int] = None
    score: Optional[float] = None
    level: Optional[PerformanceLevel] = None
    comment: Optional[str] = None

# API返回的属性
class Performance(PerformanceBase):
    id: int
    employee_id: int
    evaluator_id: int
    evaluation_date: datetime

    class Config:
        from_attributes = True

# 绩效统计
class PerformanceStatistics(BaseModel):
    department_id: int
    average_score: float
    highest_score: float
    lowest_score: float
    total_employees: int 