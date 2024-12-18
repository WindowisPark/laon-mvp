from fastapi import APIRouter

router = APIRouter()

@router.get("/entries")
def get_entries():
    return {"message": "List of entries"}
