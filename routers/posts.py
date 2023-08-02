from fastapi import APIRouter,Response,FastAPI,Depends
from sqlalchemy.orm import Session
from typing import List,Optional
import  models
import schema
from datetime import date
from database import get_db

router=APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get('/',response_model=List[schema.PostResponse])
def get_post(db: Session = Depends(get_db)):
    posts=db.query(models.Post).all()
    return posts

@router.get('/title')
def get_post(db: Session = Depends(get_db),limit:int = 10,skip:int=0,search:Optional[str]=""):
    posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts
    
  

@router.get('/{id}',response_model=List[schema.PostResponse])
def get_post(id:int,db: Session = Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id== id).first()
    return [post]

@router.get('/userposts/{uid}',response_model=List[schema.PostResponse])
def get_post(uid:int,db: Session = Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.userid == uid ).all()
    return post
 
        
@router.post('/',response_model=schema.PostResponse)
def add_post(item:schema.Posts,db: Session = Depends(get_db)):
    created=date.today()
    new_post=models.Post(createdat=created,**item.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.put('/{id}',response_model=schema.PostResponse)
def update_post(id:int,item:schema.Posts,db: Session = Depends(get_db)):
    query=db.query(models.Post).filter(models.Post.id == id)
    query.update({**item.dict()})
    db.commit()
    ret=query.first()
    return ret

@router.delete('/{id}',response_model=schema.PostResponse)
def delete_post(id:int,db: Session = Depends(get_db)):
    query=db.query(models.Post).filter(models.Post.id == id)
    ret=query
    ret=ret.first()
    query.delete()
    db.commit()
    return ret