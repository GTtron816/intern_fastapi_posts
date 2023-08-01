from fastapi import APIRouter,Response,FastAPI,Depends
from sqlalchemy.orm import Session
from typing import List
import  models
import schema
from datetime import date
from database import get_db

router=APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get('/')
def get_user(db: Session = Depends(get_db)):
    users=db.query(models.User).all()
    return users

@router.get('/{email}')
def get_user(email:str,db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.email== email).first()
    return user
     
@router.post('/',response_model=schema.UserResponse)
def add_user(item:schema.Users,db: Session = Depends(get_db)):
    created=date.today()
    new_user=models.User(createdat=created,**item.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.put('/{id}',response_model=schema.UserResponse)
def update_user(id:int,item:schema.Users,db: Session = Depends(get_db)):
    query=db.query(models.User).filter(models.User.userid == id)
    query.update({**item.dict()})
    db.commit()
    ret=query.first()
    return ret