from fastapi import APIRouter, Depends, status
from src.blog1 import blog_schemas
from src.utils.db import get_db
from sqlalchemy.orm import session
from ..services import user_service

user_router = APIRouter(prefix="/user",
                        tags = ["Users"])



@user_router.post("/", response_model=blog_schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(request: blog_schemas.UserCreate, db: session = Depends(get_db)):
    return user_service.create_user(request, db)


@user_router.get("/{id}", response_model=blog_schemas.UserWithBlogs)
def get_user(id: int, db: session = Depends(get_db)):
    return user_service.get_user(db, id)
