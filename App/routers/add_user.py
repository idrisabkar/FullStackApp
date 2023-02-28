from fastapi import APIRouter

route = APIRouter(tags=["User"])


@route.post("/user")
def add_user():
    return {"message": "add new User"}
