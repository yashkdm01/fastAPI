from pydantic import BaseModel
from typing import List
############## Blog Schemas
class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config:
        orm_mode = True


############## User Schemas

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config:
        orm_mode = True

 
class ShowBlog(BaseModel):
    id: int
    title: str
    creator: ShowUser
    class Config:
        orm_mode = True


