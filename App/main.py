import sys
from sqlalchemy.orm import Session
from App import models
sys.path.append('D:\\UI\\Python\\FastApi\\App')
from fastapi import FastAPI, Depends
from App.database import dbase, get_db, engine
from App.routers import add_user, get_user


models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(add_user.route)
app.include_router(get_user.route)


@app.on_event("startup")
async def startup():
    await dbase.connect()


@app.on_event("shutdown")
async def shutdown():
    await dbase.disconnect()


@app.get("/")
def home(db: Session = Depends(get_db)):
    return {"message": "Hello World"}
