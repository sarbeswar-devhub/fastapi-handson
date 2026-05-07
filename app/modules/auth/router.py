from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models.user import User
from app.modules.auth.schema import *
from app.modules.auth.service import *

router = APIRouter(
    tags=['Auth']
)

@router.post("/login")
def login(payload: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db), ResponseModel=LoginResponse):
    return login_user(db, payload)



@router.post("/register")
def register(payload: RegisterRequest, db: Session = Depends(get_db), ResponseModel=RegisterResponse):
    return register_user(db, payload)