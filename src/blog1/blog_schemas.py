from pydantic import BaseModel
from typing import Optional,List


class Blogbase(BaseModel):
    title : str
    body : str 
    
    
class Blog(Blogbase):
    class Config:
        orm_mode = True 
    
   
        
class  User(BaseModel):
    id : int
    name : str
    email : str
    password : str
    address : str
    phone : int
    code : int
    
class  ShowUser(BaseModel):
    name : str
    email : str
    blogs : List[Blog] = None
    
    class Config:
        orm_mode = True
        
class Showblog(BaseModel):
    title : str
    body : str
    owner : Optional[ShowUser] = None
    
    class Config:
        orm_mode = True
        
class Login(BaseModel):
    username : str
    password : str 
    
class Token(BaseModel):
    access_token : str
    token_type : str
    
class Tokendata(BaseModel):
    email : Optional[str] = None

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    blog_id: int

class Comment(CommentBase):
    id: int
    blog_id: int
    user_id: int

    class Config:
        orm_mode = True