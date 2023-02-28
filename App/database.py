import sys

sys.path.append('D:\\UI\\Python\\FastApi\\App')
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

from App.settings import variables

DATABASE_URL = f"postgresql://" \
               f"{variables.DATABASE_USERNAME}" \
               f":{variables.DATABASE_PASSWORD}@" \
               f"{variables.DATABASE_HOSTNAME}:" \
               f"{variables.DATABASE_PORT}/" \
               f"{variables.DATABASE_NAME}"
dbase = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
