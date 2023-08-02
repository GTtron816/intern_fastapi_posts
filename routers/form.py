from fastapi import APIRouter,Response,FastAPI,Depends,Form
from sqlalchemy.orm import Session
from typing import List,Optional,Annotated

router=APIRouter(
    prefix="/form",
    tags=["Form"]
)

@router.post('/')
def add_user(email: Annotated[str, Form()], password: Annotated[str, Form()]):
    new_user={"email":email,"password":password}
    return new_user