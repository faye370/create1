from sqlalchemy.orm import Session
from app.db.base import Base
from app.db.session import engine
import traceback

def init_db() -> None:
    try:
        # 创建所有表
        Base.metadata.create_all(bind=engine)
        print("数据库表创建成功！")
    except Exception as e:
        print("创建数据库表时出错：")
        print(traceback.format_exc())

if __name__ == "__main__":
    print("开始创建数据库表...")
    init_db() 