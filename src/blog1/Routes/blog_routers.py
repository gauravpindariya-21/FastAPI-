from fastapi import APIRouter, Depends, status
from src.blog1 import blog_models, blog_schemas
from src.utils.db import get_db
from sqlalchemy.orm import session
from ..services import blog_service
from src.blog1.Routes import oauth2


blog_router= APIRouter(
    prefix = "/blog",
     tags = ["Blogs"]
)



@blog_router.get("/", status_code=status.HTTP_200_OK, response_model=list[blog_schemas.BlogWithOwner])
def all(db: session = Depends(get_db), current_user: blog_models.User = Depends(oauth2.get_current_user)):
    return blog_service.list_blogs(db)
    
 
 
@blog_router.get("/{id}", status_code=status.HTTP_200_OK, response_model=blog_schemas.BlogWithOwner)
def show(id: int, db: session = Depends(get_db), current_user: blog_models.User = Depends(oauth2.get_current_user)):
    return blog_service.get_blog(db, id)


@blog_router.post("/", status_code=status.HTTP_201_CREATED, response_model=blog_schemas.BlogResponse)
def create(
    request: blog_schemas.BlogCreate,
    db: session = Depends(get_db),
    current_user: blog_models.User = Depends(oauth2.get_current_user),
):
    return blog_service.create_blog(request, db, current_user)

@blog_router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: session = Depends(get_db), current_user: blog_models.User = Depends(oauth2.get_current_user)):
    return blog_service.delete_blog(db, id, current_user)


@blog_router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=blog_schemas.BlogResponse)
def update(
    id: int,
    request: blog_schemas.BlogCreate,
    db: session = Depends(get_db),
    current_user: blog_models.User = Depends(oauth2.get_current_user),
):
    return blog_service.update_blog(db, id, request, current_user)