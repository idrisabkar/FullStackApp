from pydantic import BaseModel, EmailStr


class UserData(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserDataResponse(BaseModel):
    name: str
    email: EmailStr

    class Config:
        class Config():
            orm_mode = True
