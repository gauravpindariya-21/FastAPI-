from fastapi import APIRouter, Depends
from .. import blog_schemas
from src.utils import db
from sqlalchemy.orm import session
from fastapi.security import OAuth2PasswordRequestForm
from ..services import auth_service


authentication_router = APIRouter(
    tags = ["Authentication"]
)


@authentication_router.post("/login", response_model=blog_schemas.Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: session = Depends(db.get_db)):
    return auth_service.login_user(db, request.username, request.password)


@authentication_router.post("/refresh", response_model=blog_schemas.Token)
def refresh_token(request: blog_schemas.RefreshTokenRequest):
    return auth_service.refresh_access_token(request.refresh_token)