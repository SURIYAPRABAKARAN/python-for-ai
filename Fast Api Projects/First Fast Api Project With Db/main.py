from fastapi import FastAPI
from controller import user_controller
from enum import Enum
from jose import jwt
from datetime import datetime , timedelta
from jose import JWTError
from fastapi import HTTPException , Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

app.include_router(user_controller.router)

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

class LoginRequest(BaseModel):
    email: str
    

@app.get("/")
def sample_enpoint():
    return {"message": f"welcome to fast api to db : {ModelName.alexnet}"}

@app.post("/login")
def login(loginRequest: LoginRequest):

    token = create_token({"sub": loginRequest.email})
    
    print(f"token : {token}")

    return {"access_token": token}

def create_token(data: dict):
    to_encode = data.copy()
    
    print(f"to_encode : {to_encode}")

    expire = datetime.utcnow() + timedelta(minutes=1)
    
    print(f"expire : {expire}")

    to_encode.update({"exp": expire})
    
    print(f"to_encode after expire : {to_encode}")

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.get("/secure")
def secure_api(token: str = Depends(oauth2_scheme)):

    user = verify_token(token)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    print(f"user : {user}")

    return {"message": f"Hello {user}"}

def verify_token(token: str):
    try:
        print("Received token:", token)

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        print("Decoded payload:", payload)

        email = payload.get("sub")
        return email

    except JWTError as e:
        print("JWT ERROR:", str(e))
        return None