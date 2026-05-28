from sqlalchemy.orm import session

from src.blog1 import blog_schemas
from src.blog1.repository import user
from src.utils.hashing import Hash


def create_user(request: blog_schemas.UserCreate, db: session):
    return user.create(request, db, Hash)


def get_user(db: session, user_id: int):
    return user.get(db, user_id)
