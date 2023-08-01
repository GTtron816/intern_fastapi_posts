from pydantic import BaseModel
from datetime import date
class Users(BaseModel):
    email:str
    password:str
class Posts(BaseModel):
    userid:int
    title:str
    content:str
    published:bool
    
class UserResponse(BaseModel):
    userid:int
    email:str
    createdat:date
    class Config:
        orm_mode=True
class PostResponse(BaseModel):
    id:int
    title:str
    content: str
    userid: int
    published: bool
    createdat: date
    user:UserResponse
    class Config:
        orm_mode=True
    