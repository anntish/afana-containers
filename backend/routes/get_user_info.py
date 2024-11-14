from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.models import User
from sqlalchemy.orm import Session
from models.init_db import SessionLocal

router = APIRouter()

class UserInfo(BaseModel):
    user_name: str
    user_surname: str
    user_job: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/user_info/")
async def process_user_info(data: UserInfo, db: Session = Depends(get_db)):
    user_prompt = User(
        user_name=data.user_name,
        user_surname=data.user_surname,
        user_job=data.user_job
    )
    db.add(user_prompt)
    db.commit()

    response = {
        "message": "Successfully"
    }

    return response