from sqlalchemy.orm import session, joinedload
from src.blog1 import blog_models, blog_schemas
from fastapi import HTTPException , status


def get_all(db : session):
    blogs = db.query(blog_models.Blog).all()
    return blogs


def show(db : session, id : int):
    blog = db.query(blog_models.Blog).options(joinedload(blog_models.Blog.owner)).filter(blog_models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"blog with the id {id} is not available")
    
    return blog


def create(db : session, request: blog_schemas.Blog, user_id: int):
    new_blog = blog_models.Blog(title = request.title , body = request.body, user_id = user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(db : session, id : int):
    blog=db.query(blog_models.Blog).filter(blog_models.Blog.id ==id)
    
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"blog with the id {id} is not available")
    
    blog.delete(synchronize_session = False)
    db.commit()
    return {"data":f"blog with the id {id} is deleted successfully"}

def update(db : session, id, request  :blog_schemas.Blog):
    blog = db.query(blog_models.Blog).filter(blog_models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"blog with the id {id} is not available")
    
    blog_data = request.dict()  # Convert request to dictionary
    blog.update(blog_data)
    db.commit()
    return {"data":f"blog with the id {id} is updated successfully"}