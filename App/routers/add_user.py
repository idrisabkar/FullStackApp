from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from App.database import get_db
from App.schemas import UserData
from App.models import Users

route = APIRouter(tags=["User"])


@route.post("/user")
def add_user(data: UserData, db: Session = Depends(get_db)):
    new_user = Users(**data.dict())
    db.add(new_user)
    db.commit()
    return {"message": "add new User"}
