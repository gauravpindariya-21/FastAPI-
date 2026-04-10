from fastapi import APIRouter, Depends, status, HTTPException
from src.blog1 import blog_schemas, blog_models
from src.utils.db import get_db
from sqlalchemy.orm import session, joinedload 
from ..repository import blog
from src.blog1.Routes import oauth2


blog_router= APIRouter(
    prefix = "/blog",
     tags = ["Blogs"]
)



@blog_router.get("/", status_code = status.HTTP_200_OK , response_model=list[blog_schemas.Showblog])
def all(db:session =Depends(get_db),current_user: blog_schemas.User = Depends(oauth2.get_curent_user), search: str = None):
    return blog.get_all(db, search)
    
 
 
@blog_router.get("/{id}", status_code = status.HTTP_200_OK, response_model=blog_schemas.Showblog)
def show(id : int,db : session = Depends(get_db),current_user: blog_schemas.User = Depends(oauth2.get_curent_user)):
    return blog.show(db, id)

@blog_router.post("/", status_code = status.HTTP_201_CREATED)
def create (request : blog_schemas.Blog, db:session = Depends(get_db),current_user: blog_schemas.User = Depends(oauth2.get_curent_user)):
    return blog.create(db, request, current_user.id)

@blog_router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def destroy(id : int, db:session = Depends(get_db),current_user: blog_schemas.User = Depends(oauth2.get_curent_user)):
    return blog.destroy(db, id)

@blog_router.put("/{id}", status_code = status.HTTP_202_ACCEPTED)
def update(id : int,request : blog_schemas.Blog, db : session = Depends(get_db),current_user: blog_schemas.User = Depends(oauth2.get_curent_user)):
    return blog.update(db, id, request)