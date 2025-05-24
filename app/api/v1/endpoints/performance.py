from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Performance])
def read_performance_records(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    employee_id: Optional[int] = None,
    year: Optional[int] = None,
    month: Optional[int] = None,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    获取绩效记录列表
    """
    performance_records = crud.performance.get_multi(
        db,
        skip=skip,
        limit=limit,
        employee_id=employee_id,
        year=year,
        month=month
    )
    return performance_records

@router.post("/", response_model=schemas.Performance)
def create_performance(
    *,
    db: Session = Depends(deps.get_db),
    performance_in: schemas.PerformanceCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    """
    创建绩效记录
    """
    performance = crud.performance.create(
        db=db,
        obj_in=performance_in,
        evaluator_id=current_user.employee.id
    )
    return performance

@router.get("/{performance_id}", response_model=schemas.Performance)
def read_performance(
    *,
    db: Session = Depends(deps.get_db),
    performance_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    获取指定绩效记录
    """
    performance = crud.performance.get(db=db, id=performance_id)
    if not performance:
        raise HTTPException(status_code=404, detail="绩效记录不存在")
    return performance

@router.put("/{performance_id}", response_model=schemas.Performance)
def update_performance(
    *,
    db: Session = Depends(deps.get_db),
    performance_id: int,
    performance_in: schemas.PerformanceUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    """
    更新绩效记录
    """
    performance = crud.performance.get(db=db, id=performance_id)
    if not performance:
        raise HTTPException(status_code=404, detail="绩效记录不存在")
    performance = crud.performance.update(
        db=db,
        db_obj=performance,
        obj_in=performance_in
    )
    return performance

@router.get("/statistics/department/{department_id}", response_model=schemas.PerformanceStatistics)
def get_department_statistics(
    *,
    db: Session = Depends(deps.get_db),
    department_id: int,
    year: int,
    month: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    """
    获取部门绩效统计
    """
    statistics = crud.performance.get_department_statistics(
        db=db,
        department_id=department_id,
        year=year,
        month=month
    )
    return statistics 