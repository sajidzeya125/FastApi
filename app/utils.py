from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from . import database, models, schemas






oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "a7f8c3b9e2d1a4f6c5b8e9a2d3f4c5b6e7a8b9c0d1e2f3a4b5c6d7e8f9a0b"
ALGORITHM = "HS256"

def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    # to create a token we need to encode the data using a secret key and an algorithm
    # we can use the jwt library to do this
    create_access_token = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=30)
    create_access_token.update({"exp": expire})

    
    
    
    
    encoded_jwt = jwt.encode(create_access_token, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"Decoded payload: {payload}") 
        id: str = payload.get("user_id")
        if id is None:
            print("user_id not found in token")
            raise credentials_exception
        
    except jwt.PyJWTError as e:
        print(f"JWT Error: {e}") 
        raise credentials_exception
    return int(id)
    
    

    
    
    
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)): 
    print(f"Token received: {token}")    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token).first()
    return user