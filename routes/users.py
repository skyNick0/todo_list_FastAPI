from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

from bd.todo_database import get_db
from bd.models import User
from bd.pd_models import UserCreate

router = APIRouter()

@router.post("/new_user")
def create_user(user:UserCreate , db: Session = Depends(get_db)):
    new_user = User(
        username=user.username,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



