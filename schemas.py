from pydantic import BaseModel
from typing import List, Optional
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


class Login(BaseModel):
    username: str
    password: str
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True


class TokenData(BaseModel):
    email: Optional[str] = None