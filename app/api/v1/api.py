from fastapi import APIRouter
from app.api.v1.endpoints import auth, employees, attendance, performance

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["认证"])
api_router.include_router(employees.router, prefix="/employees", tags=["员工管理"])
api_router.include_router(attendance.router, prefix="/attendance", tags=["考勤管理"])
api_router.include_router(performance.router, prefix="/performance", tags=["绩效管理"]) 