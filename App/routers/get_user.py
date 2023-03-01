from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session
from App.database import get_db
from App.schemas import UserDataResponse
from App.models import Users

route = APIRouter(prefix="/user", tags=["User"])


@route.get("/{user_id}", response_model=UserDataResponse, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The user_id that you provided doesn't exists")
    return {**user.__dict__}


@route.get("", response_model=UserDataResponse, status_code=status.HTTP_200_OK)
def get_user(email: dict, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.email == email["email"]).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The email that you provided doesn't exists")
    return {**user.__dict__}
