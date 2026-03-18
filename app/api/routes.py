from fastapi import APIRouter

router = APIRouter()

@router.get("/quote")
def get_quote():
    return {"message": "random quote"}