from sqlalchemy import Column, Integer, String, Boolean ,Date, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
class Post(Base):
    __tablename__ = "posts"
    id=Column(Integer, primary_key=True, index=True)
    userid=Column(Integer,ForeignKey("users.userid"))
    title=Column(String)
    content=Column(String)
    published=Column(Boolean)
    createdat=Column(Date)
    user=relationship("User")
class User(Base):
    __tablename__ = "users"
    userid=Column(Integer, primary_key=True, index=True)
    email=Column(String)
    password=Column(String)
    createdat=Column(Date)
    