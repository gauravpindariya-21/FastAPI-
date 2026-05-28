from fastapi import HTTPException, status
from sqlalchemy.orm import session

from src.blog1 import blog_models, token
from src.utils.hashing import Hash


def login_user(db: session, username: str, password: str):
    user = db.query(blog_models.User).filter(blog_models.User.email == username).first()
    if not user or not Hash.verify(user.password, password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = token.create_access_token(data={"sub": user.email})
    refresh_token = token.create_refresh_token(data={"sub": user.email})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


def refresh_access_token(refresh_token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid refresh token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = token.verify_token(refresh_token, credentials_exception, expected_type="refresh")
    access_token = token.create_access_token(data={"sub": token_data.email})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}
