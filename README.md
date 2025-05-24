企业人员管理系统

1、项目简介
这是一个基于Python FastAPI开发的企业级人员管理系统，提供员工信息管理、考勤管理、绩效管理等功能。

2、技术栈
后端：FastAPI
数据库：MySQL
ORM：SQLAlchemy
认证：JWT
文档：Swagger/OpenAPI

2、功能模块
1. 员工信息管理
2. 考勤管理
3. 绩效管理
4. 系统管理

3、安装说明
1） 创建虚拟环境：
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

2）安装依赖：
pip install -r requirements.txt

3） 配置环境变量：
复制 .env.example 到 .env并修改相应配置

4）初始化数据库：
alembic upgrade head

5）启动服务：
uvicorn app.main:app --reload

4、API文档
启动服务后访问：http://localhost:8000/docs

5、开发团队
开发人员
测试团队
项目经理

6、许可证
MIT 
