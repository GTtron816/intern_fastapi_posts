from pydantic import BaseModel
class Posts(BaseModel):
    userid:int
    title:str
    content:str
    published:bool
class Users(BaseModel):
    email:str
    password:str
class PostResponse(BaseModel):
    id:int
    title:str
    class Config:
        orm_mode=True
class UserResponse(BaseModel):
    userid:int
    email:str
    class Config:
        orm_mode=True
   
    