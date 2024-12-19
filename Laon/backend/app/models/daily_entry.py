from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base

# 하루 기록 테이블 모델
class DailyEntry(Base):
    __tablename__ = "daily_entries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String(500), nullable=False)  # 기록 내용
    emotion_result = Column(String(50), nullable=True)  # 감정 분석 결과
    created_at = Column(DateTime, default=datetime.utcnow)  # 생성 시간
