from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

API_KEY = "123_ABC_"
# secure a API with API key
@app.middleware("http")
async def check_api_key(request,call_next):
    key = request.headers.get("API_KEY")
    if key != API_KEY:
        return JSONResponse(status_code=401,content={"error":"unauthorized"})
    else:
        return await call_next(request)
 
   

@app.get("/")
def home_get():
    return {"message": "Hello, FastAPI!"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Surya"}

class User(BaseModel):
    name : str
    age : int

users = []

@app.post("/create_user")
def create_user(user: User):
    users.append(user)
    print(f"user added and total users : {len(users)}")
    return {
        "message": "User created",
        "name": user.name,
        "age": user.age
    }