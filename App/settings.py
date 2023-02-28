from pydantic import BaseSettings


class Variables(BaseSettings):
    DATABASE_NAME: str
    DATABASE_HOSTNAME: str
    DATABASE_PORT: int
    DATABASE_PASSWORD: str
    DATABASE_USERNAME: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"


variables = Variables()
