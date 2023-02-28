from pydantic import BaseModel, EmailStr


class UserData(BaseModel):
    user_name: str
    email: EmailStr
    password: str


class UserDataResponse(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
