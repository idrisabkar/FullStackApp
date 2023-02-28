from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from App.database import get_db
from App.schemas import UserData
from App.models import Users

route = APIRouter(tags=["User"])


@route.post("/user", status_code=status.HTTP_200_OK)
def add_user(data: UserData, db: Session = Depends(get_db)):
    try:
        new_user = Users(**data.dict())
        db.add(new_user)
        db.commit()
    except Exception:
        raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, detail=Exception)
    return {"status": status.HTTP_200_OK, "message": "User Successfully Created"}
