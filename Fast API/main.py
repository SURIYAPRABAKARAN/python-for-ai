from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home_get():
    return {"message": "Hello, FastAPI!"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Surya"}

class User(BaseModel):
    name : str
    age : int

@app.post("/create_user")
def create_user(user: User):
    return {
        "message": "User created",
        "name": user.name,
        "age": user.age
    }