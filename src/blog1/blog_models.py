from src.utils.db import Base
from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key = True , index =True)
    title = Column(String)
    body  = Column(String)
    user_id = Column(Integer ,ForeignKey("users.id") )
    
    owner = relationship ("User", back_populates = "blogs" )
    comments = relationship("Comment", back_populates="blog")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True , index = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    address = Column(String)
    phone = Column(Integer)
    code = Column(Integer)
    
    blogs = relationship("Blog" , back_populates = "owner")
    comments = relationship("Comment", back_populates="commenter")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    blog = relationship("Blog", back_populates="comments")
    commenter = relationship("User", back_populates="comments")