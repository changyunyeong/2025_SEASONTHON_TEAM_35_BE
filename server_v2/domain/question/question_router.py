from fastapi import APIRouter

from database import SessionLocal
from models import Question

router = APIRouter(
    prefix="/question", # spring controller
)

@router.get("/list")
def question_list():
    db = SessionLocal()
    _question_list = db.query(Question).order_by(Question.created_at.desc()).all()
    db.close()
    return _question_list