from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.core.oauth2 import get_current_user
from app.modules.user import schema, service
from app.db.database import get_db


router = APIRouter(
    tags=["user"],
    prefix="/user"
)


@router.get("/list", response_model=schema.UserListRepoonse)
def get_user_list(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return service.fetch_users(db, user)

@router.get("/{id}", response_model=schema.UserResponse)
def get_user(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return service.fetch_users(db, id)

@router.get("/profile", response_model=schema.UserResponse)
def get_user_profile(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return service.fetch_users(db, user.id)