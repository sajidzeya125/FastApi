from fastapi import FastAPI, Response,status,HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, get_db, Base
from sqlalchemy.orm import Session
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)




app = FastAPI()




      
while True:    
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi-course',
                            user='postgres', password='postgres', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull")
        break
    except Exception as error:
        print("Connection with database has been failed")
        print("Error:", error)
        time.sleep(3)
            

    
    
my_posts=[{"title": "My First Post","content": "Guys this is my first post please support and follow me in my journey","id":1},
          {"title": "Online Games","content": "We provide an integrated platform for playing various online games","id":2}]


def find_posts(id):
    for p in my_posts:
        if p['id']==id:
            return p
        
        
        
def find_post_index(id):
    for i, p in enumerate(my_posts):
        if p['id']==id:
            return i        
    


# @app.get("/posts/vote")
# def read_root():
#     return {"message": " Hello World"}

# @app.get("/sqlalchemy")
# def read_sqlalchemy(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"data": posts}


# @app.get("/items/{item_id}/{q}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

