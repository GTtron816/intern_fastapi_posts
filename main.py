from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import  models
import schema
from datetime import date

from database import SessionLocal, engine,get_db


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
    
app=FastAPI()
origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/posts')
def get_user(db: Session = Depends(get_db)):
    posts=db.query(models.Post).all()
    return posts
    
  

@app.get('/posts/{id}')
def get_user(id:int,db: Session = Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id== id).first()
    return [post]
 
        
@app.post('/posts',response_model=schema.PostResponse)
def add_post(item:schema.Posts,db: Session = Depends(get_db)):
    created=date.today()
    new_post=models.Post(createdat=created,**item.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.put('/posts/{id}',response_model=schema.PostResponse)
def update_post(id:int,item:schema.Posts,db: Session = Depends(get_db)):
    query=db.query(models.Post).filter(models.Post.id == id)
    query.update({**item.dict()})
    db.commit()
    ret=query.first()
    return ret

@app.delete('/posts/{id}')
def delete_post(id:int,db: Session = Depends(get_db)):
    query=db.query(models.Post).filter(models.Post.id == id)
    query.delete()
    db.commit()
   
@app.get('/users')
def get_user(db: Session = Depends(get_db)):
    users=db.query(models.User).all()
    return users

@app.get('/users/{id}')
def get_user(id:int,db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.userid== id).first()
    return [user]
     
@app.post('/users',response_model=schema.UserResponse)
def add_user(item:schema.Users,db: Session = Depends(get_db)):
    created=date.today()
    new_user=models.User(createdat=created,**item.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.put('/users/{id}',response_model=schema.UserResponse)
def update_user(id:int,item:schema.Users,db: Session = Depends(get_db)):
    query=db.query(models.User).filter(models.User.userid == id)
    query.update({**item.dict()})
    db.commit()
    ret=query.first()
    return ret