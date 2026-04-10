from sqlalchemy.orm import Session
from src.blog1 import blog_models, blog_schemas
from fastapi import HTTPException, status

def create(db: Session, request: blog_schemas.CommentCreate, user_id: int):
    new_comment = blog_models.Comment(text=request.text, blog_id=request.blog_id, user_id=user_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_by_blog(db: Session, blog_id: int):
    return db.query(blog_models.Comment).filter(blog_models.Comment.blog_id == blog_id).all()
