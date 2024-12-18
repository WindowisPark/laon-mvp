from fastapi import FastAPI
from app.routes.daily_entry import router as entry_router  # API 라우트를 불러옴
from app.core.database import Base, engine  # DB 초기화

# FastAPI 애플리케이션 생성
app = FastAPI()

# 데이터베이스 테이블 생성
@app.on_event("startup")
def startup_event():
    print("Creating database tables if they do not exist...")
    Base.metadata.create_all(bind=engine)

# 기본 라우트 추가
@app.get("/health")
def health_check():
    return {"status": "ok"}

# 다른 라우트 등록
app.include_router(entry_router, prefix="/api/v1")
