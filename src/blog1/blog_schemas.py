from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class BlogBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    body: str = Field(..., min_length=1)


class BlogCreate(BlogBase):
    pass


class BlogResponse(BlogBase):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)


class BlogPreview(BlogBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)
    address: str = Field(..., min_length=3, max_length=200)
    phone: int
    code: int


class UserSummary(BaseModel):
    id: int
    name: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: str
    phone: int
    code: int
    model_config = ConfigDict(from_attributes=True)


class UserWithBlogs(UserResponse):
    blogs: list[BlogPreview] = Field(default_factory=list)


class BlogWithOwner(BlogBase):
    id: int
    owner: Optional[UserSummary] = None
    model_config = ConfigDict(from_attributes=True)


class Login(BaseModel):
    username: EmailStr
    password: str = Field(..., min_length=8)


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class Tokendata(BaseModel):
    email: Optional[str] = None
    token_type: Optional[str] = None