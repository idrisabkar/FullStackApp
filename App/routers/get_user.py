from fastapi import APIRouter

route = APIRouter(prefix="/user", tags=["User"])


@route.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
