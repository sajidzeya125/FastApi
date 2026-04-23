

from datetime import datetime as dateandtime
from typing import Optional
from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    published: bool=True

class PostCreate(PostBase):
    pass



class Post(PostBase):
    id: int
    created_at: dateandtime
    
    class Config:
        orm_mode = True   
        
        
        
class usercreate(BaseModel):
    email: EmailStr
    password: str

class userout(BaseModel):
    id: int
    email: EmailStr
    created_at: dateandtime
    

    class Config:
        orm_mode = True
        
        
class userlogin(BaseModel):
    email: EmailStr
    password: str 
    
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
    
class tokenData(BaseModel):
    id: Optional[str] = None              
