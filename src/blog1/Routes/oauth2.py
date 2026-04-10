from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from src.blog1 import token, blog_models
from src.utils.db import get_db
from sqlalchemy.orm import Session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_curent_user(data : str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate  credentials",
        headers = {"WWW-Authenticate" : "Bearer"},
    )
    
    token_data = token.verify_token(data, credentials_exception)
    user = db.query(blog_models.User).filter(blog_models.User.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    return user