from sqlalchemy.orm import joinedload, session
from src.blog1 import blog_models, blog_schemas
from fastapi import HTTPException, status


def get_all(db: session):
    blogs = db.query(blog_models.Blog).options(joinedload(blog_models.Blog.owner)).all()
    return blogs


def show(db: session, id: int):
    blog = db.query(blog_models.Blog).options(joinedload(blog_models.Blog.owner)).filter(blog_models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")

    return blog


def create(db: session, request: blog_schemas.BlogCreate, user_id: int):
    new_blog = blog_models.Blog(title=request.title, body=request.body, user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(db: session, id: int, current_user_id: int):
    blog = db.query(blog_models.Blog).filter(blog_models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")

    if blog.first().user_id != current_user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this blog")

    blog.delete(synchronize_session=False)
    db.commit()
    return None


def update(db: session, id: int, request: blog_schemas.BlogCreate, current_user_id: int):
    blog = db.query(blog_models.Blog).filter(blog_models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")

    if blog.first().user_id != current_user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update this blog")

    blog_data = request.model_dump()
    blog.update(blog_data)
    db.commit()
    updated_blog = blog.first()
    db.refresh(updated_blog)
    return updated_blog