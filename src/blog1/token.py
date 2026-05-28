from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from . import blog_schemas
from src.core.config import settings


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt


def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.refresh_token_expire_minutes)
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt


def verify_token(token: str, credentials_exception, expected_type: str = "access"):
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        email: str = payload.get("sub")
        token_type: str = payload.get("type")
        if email is None:
            raise credentials_exception
        if token_type != expected_type:
            raise credentials_exception
        token_data = blog_schemas.Tokendata(email=email, token_type=token_type)
        return token_data
    except JWTError:
        raise credentials_exception