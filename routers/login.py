from fastapi import APIRouter,Response,FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from typing import List
import  models
import schema
from datetime import date
from database import get_db
from utils import verify

router=APIRouter(
    prefix="/login",
    tags=["Login"]
)

@router.post('/')
def get_user(item:schema.Users,db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.email== item.email).first()
    if not user:
        raise HTTPException(status_code=403, detail="Invalid Credentials")
    user_verify=verify(item.password,user.password)
    
    if not user_verify:
        raise HTTPException(status_code=403, detail="Invalid Password")
    else:
        raise HTTPException(status_code=200, detail="Validation Success")
        