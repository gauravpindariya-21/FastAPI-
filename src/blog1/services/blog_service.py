from sqlalchemy.orm import session

from src.blog1 import blog_models, blog_schemas
from src.blog1.repository import blog


def list_blogs(db: session):
    return blog.get_all(db)


def get_blog(db: session, blog_id: int):
    return blog.show(db, blog_id)


def create_blog(request: blog_schemas.BlogCreate, db: session, current_user: blog_models.User):
    return blog.create(db, request, current_user.id)


def delete_blog(db: session, blog_id: int, current_user: blog_models.User):
    return blog.destroy(db, blog_id, current_user.id)


def update_blog(db: session, blog_id: int, request: blog_schemas.BlogCreate, current_user: blog_models.User):
    return blog.update(db, blog_id, request, current_user.id)
