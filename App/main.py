from fastapi import FastAPI

from App.routers import add_user, get_user

app = FastAPI()

app.include_router(add_user.route)
app.include_router(get_user.route)


@app.get("/")
def home():
    return {"message": "Hello World"}
