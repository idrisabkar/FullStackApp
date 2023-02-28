from fastapi import FastAPI

from App.database.database import dbase
from App.routers import add_user, get_user

app = FastAPI()

app.include_router(add_user.route)
app.include_router(get_user.route)


@app.on_event("startup")
async def startup():
    from App.database import database
    await dbase.connect()


@app.on_event("shutdown")
async def shutdown():
    await dbase.disconnect()


@app.get("/")
def home():
    return {"message": "Hello World"}
