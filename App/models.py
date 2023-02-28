import sys
sys.path.append('D:\\UI\\Python\\FastApi\\App')
from App.database import Base
from sqlalchemy import String, Integer, Column, DateTime, func


class Users(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    __table_args__ = {"extend_existing": True}
