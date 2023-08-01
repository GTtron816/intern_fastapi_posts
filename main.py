from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import  models
import schema
from datetime import date
from routers import users,posts

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






   
app.include_router(users.router)
app.include_router(posts.router)