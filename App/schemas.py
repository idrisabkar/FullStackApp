from pydantic import BaseModel, EmailStr


class UserData(BaseModel):
    user_name: str
    email: EmailStr
    password: str


class UserDataResponse(BaseModel):
    user_name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
