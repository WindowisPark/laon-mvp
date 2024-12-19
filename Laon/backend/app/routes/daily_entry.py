from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.daily_entry import DailyEntry
from app.core.database import SessionLocal
from pydantic import BaseModel

router = APIRouter()

# DB 세션 생성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 요청 본문 데이터 모델
class EntryCreate(BaseModel):
    text: str
    
# 기록 저장 (CREATE)
@router.post("/entries")
def create_entry(entry: EntryCreate, db: Session = Depends(get_db)):
    new_entry = DailyEntry(text=entry.text, emotion_result=None)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

# 전체 기록 조회 (READ)
@router.get("/entries")
def get_entries(db: Session = Depends(get_db)):
    return db.query(DailyEntry).all()

# 특정 기록 조회 (READ)
@router.get("/entries/{entry_id}")
def get_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = db.query(DailyEntry).filter(DailyEntry.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry

# 기록 수정 (UPDATE)
@router.put("/entries/{entry_id}")
def update_entry(entry_id: int, updated_entry: EntryCreate, db: Session = Depends(get_db)):
    entry = db.query(DailyEntry).filter(DailyEntry.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    entry.text = updated_entry.text  # 수정된 텍스트로 업데이트
    db.commit()
    db.refresh(entry)
    return entry

# 기록 삭제 (DELETE)
@router.delete("/entries/{entry_id}")
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = db.query(DailyEntry).filter(DailyEntry.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    db.delete(entry)
    db.commit()
    return {"detail": f"Entry with id {entry_id} deleted"}
