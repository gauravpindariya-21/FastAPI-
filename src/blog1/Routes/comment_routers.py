from fastapi import APIRouter, Depends, status
from src.blog1 import blog_schemas, blog_models
from src.utils.db import get_db
from sqlalchemy.orm import Session
from ..repository import comment
from src.blog1.Routes import oauth2
from typing import List

comment_router = APIRouter(
    prefix="/comment",
    tags=["Comments"]
)

@comment_router.post("/", status_code=status.HTTP_201_CREATED, response_model=blog_schemas.Comment)
def create(request: blog_schemas.CommentCreate, db: Session = Depends(get_db), current_user: blog_models.User = Depends(oauth2.get_curent_user)):
    return comment.create(db, request, current_user.id)

@comment_router.get("/{blog_id}", response_model=List[blog_schemas.Comment])
def get_comments(blog_id: int, db: Session = Depends(get_db), current_user: blog_models.User = Depends(oauth2.get_curent_user)):
    return comment.get_by_blog(db, blog_id)
