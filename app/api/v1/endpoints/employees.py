from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Employee])
def read_employees(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    department_id: Optional[int] = None,
    status: Optional[bool] = None,
):
    """
    获取员工列表
    """
    employees = crud.employee.get_multi(
        db, skip=skip, limit=limit, department_id=department_id, status=status
    )
    return employees

@router.post("/", response_model=schemas.Employee)
def create_employee(
    *,
    db: Session = Depends(deps.get_db),
    employee_in: schemas.EmployeeCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    """
    创建新员工
    """
    employee = crud.employee.create(db=db, obj_in=employee_in)
    return employee

@router.get("/{employee_id}", response_model=schemas.Employee)
def read_employee(
    *,
    db: Session = Depends(deps.get_db),
    employee_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    获取指定员工信息
    """
    employee = crud.employee.get(db=db, id=employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="员工不存在")
    return employee

@router.put("/{employee_id}", response_model=schemas.Employee)
def update_employee(
    *,
    db: Session = Depends(deps.get_db),
    employee_id: int,
    employee_in: schemas.EmployeeUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    """
    更新员工信息
    """
    employee = crud.employee.get(db=db, id=employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="员工不存在")
    employee = crud.employee.update(db=db, db_obj=employee, obj_in=employee_in)
    return employee

@router.delete("/{employee_id}")
def delete_employee(
    *,
    db: Session = Depends(deps.get_db),
    employee_id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    """
    删除员工（标记为离职）
    """
    employee = crud.employee.get(db=db, id=employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="员工不存在")
    employee = crud.employee.remove(db=db, id=employee_id)
    return {"msg": "员工已标记为离职"} 