from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

from .config import Settings
from . import models, schemas, utils
from .database import engine
from sqlalchemy.orm import Session
from .routers import post, user, auth, vote






# models.Base.metadata.create_all(bind=engine)


app = FastAPI()
origins = ["https://www.google.com"]  # You can specify allowed origins here, e.g., ["http://localhost:3000"]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}