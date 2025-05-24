from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps
from datetime import datetime, date

router = APIRouter()

@router.get("/", response_model=List[schemas.Attendance])
def read_attendance_records(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    employee_id: Optional[int] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    status: Optional[str] = None,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    获取考勤记录列表
    """
    attendance_records = crud.attendance.get_multi(
        db,
        skip=skip,
        limit=limit,
        employee_id=employee_id,
        start_date=start_date,
        end_date=end_date,
        status=status
    )
    return attendance_records

@router.post("/check-in", response_model=schemas.Attendance)
def create_check_in(
    *,
    db: Session = Depends(deps.get_db),
    attendance_in: schemas.AttendanceCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    创建签到记录
    """
    attendance = crud.attendance.create_check_in(
        db=db,
        obj_in=attendance_in,
        employee_id=current_user.employee.id
    )
    return attendance

@router.post("/check-out", response_model=schemas.Attendance)
def create_check_out(
    *,
    db: Session = Depends(deps.get_db),
    attendance_in: schemas.AttendanceCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    创建签退记录
    """
    attendance = crud.attendance.create_check_out(
        db=db,
        obj_in=attendance_in,
        employee_id=current_user.employee.id
    )
    return attendance

@router.post("/leave", response_model=schemas.Attendance)
def create_leave_request(
    *,
    db: Session = Depends(deps.get_db),
    leave_in: schemas.LeaveCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    创建请假申请
    """
    leave = crud.attendance.create_leave(
        db=db,
        obj_in=leave_in,
        employee_id=current_user.employee.id
    )
    return leave

@router.put("/{attendance_id}/approve", response_model=schemas.Attendance)
def approve_attendance(
    *,
    db: Session = Depends(deps.get_db),
    attendance_id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    """
    审批考勤记录
    """
    attendance = crud.attendance.get(db=db, id=attendance_id)
    if not attendance:
        raise HTTPException(status_code=404, detail="考勤记录不存在")
    attendance = crud.attendance.approve(db=db, db_obj=attendance)
    return attendance

@router.put("/{attendance_id}/reject", response_model=schemas.Attendance)
def reject_attendance(
    *,
    db: Session = Depends(deps.get_db),
    attendance_id: int,
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    """
    拒绝考勤记录
    """
    attendance = crud.attendance.get(db=db, id=attendance_id)
    if not attendance:
        raise HTTPException(status_code=404, detail="考勤记录不存在")
    attendance = crud.attendance.reject(db=db, db_obj=attendance)
    return attendance 