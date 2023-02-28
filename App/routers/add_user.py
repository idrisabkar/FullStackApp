import sqlalchemy
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.dialects.postgresql import psycopg2
from sqlalchemy.orm import Session
from App.database import get_db
from App.schemas import UserData
from App.models import Users
from sqlalchemy.exc import IntegrityError

route = APIRouter(tags=["User"])


@route.post("/user", status_code=status.HTTP_200_OK)
def add_user(data: UserData, db: Session = Depends(get_db)):
    try:
        print("i'm here")
        new_user = Users(**data.dict())
        db.add(new_user)
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_226_IM_USED,
                            detail="the email that you provided exists" if 'duplicate key value violates '
                                                                           'unique constraint '
                                                                           '"user_email_key"' in str(e)
                            else "Error adding user")
    return {"status": status.HTTP_200_OK, "message": "User Successfully Created"}
