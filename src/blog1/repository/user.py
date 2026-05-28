from fastapi import HTTPException, status
from sqlalchemy.orm import joinedload, session

from src.blog1 import blog_models, blog_schemas


def create(request: blog_schemas.UserCreate, db: session, hash_service):
    existing_user = db.query(blog_models.User).filter(blog_models.User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    new_user = blog_models.User(
        name=request.name,
        email=request.email,
        address=request.address,
        phone=request.phone,
        code=request.code,
    )
    setattr(new_user, "password", hash_service.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(db: session, id: int):
    user = db.query(blog_models.User).options(joinedload(blog_models.User.blogs)).filter(blog_models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    return user
