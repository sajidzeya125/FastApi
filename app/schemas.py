

from datetime import datetime as dateandtime
from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, Field


class PostBase(BaseModel):
    title: str
    content: str
    published: bool=True

class PostCreate(PostBase):
    pass


class userout(BaseModel):
    id: int
    email: EmailStr
    created_at: dateandtime
    

    class Config:
        orm_mode = True



class Post(PostBase):
    id: int
    created_at: dateandtime
    user_id: int
    user: userout

    class Config:
        orm_mode = True 

class PostOut(BaseModel):
    Post: Post

    vote_count: int

    class Config:
        orm_mode = True         
        
        
        
class usercreate(BaseModel):
    email: EmailStr
    password: str


        
        
class userlogin(BaseModel):
    email: EmailStr
    password: str 
    
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
    
class tokenData(BaseModel):
    id: Optional[str] = None 



class vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]
