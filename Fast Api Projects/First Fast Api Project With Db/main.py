from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, field_validator
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import os

app = FastAPI()

# =========================
# CONFIG (Move to .env in real apps)
# =========================
SECRET_KEY = "mysecretkey"   # 👉 use os.getenv("SECRET_KEY") in real apps
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# =========================
# SECURITY SETUP
# =========================
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# =========================
# MODELS
# =========================
class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    email: str
    password: str

    @field_validator('password')
    @classmethod
    def truncate_password(cls, v: str):
        return v[:72]  # bcrypt limit

# =========================
# FAKE DB (Replace with real DB later)
# =========================
fake_db = {
    "suriya@gmail.com": {
        "email": "suriya@gmail.com",
        "password": pwd_context.hash("1234")
    }
}

# =========================
# PASSWORD FUNCTIONS
# =========================
def hash_password(password: str):
    return pwd_context.hash(password[:72])

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# =========================
# JWT FUNCTIONS
# =========================
def create_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        email = payload.get("sub")
        if not email:
            return None

        # ✅ Check if user still exists
        user = fake_db.get(email)
        if not user:
            return None

        return email

    except JWTError as e:
        print("JWT ERROR:", str(e))
        return None

# =========================
# API ENDPOINTS
# =========================

@app.get("/")
def home():
    return {"message": "Welcome to Secure FastAPI 🚀"}

# 🔐 REGISTER
@app.post("/register")
def register(request: RegisterRequest):

    if request.email in fake_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_pwd = hash_password(request.password)

    fake_db[request.email] = {
        "email": request.email,
        "password": hashed_pwd
    }

    return {"message": "User registered successfully"}

# 🔐 LOGIN
@app.post("/login")
def login(request: LoginRequest):

    user = fake_db.get(request.email)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(request.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_token({"sub": request.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

# 🔐 SECURE API
@app.get("/secure")
def secure_api(token: str = Depends(oauth2_scheme)):

    user = verify_token(token)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return {"message": f"Hello {user}, you are authorized ✅"}


# =========================

# 🔐 SIMPLE JWT FLOW (EASY)

# =========================

# 1️⃣ REGISTER

# -----------------

# API: POST /register

# Body:

# {

# "email": "[test@gmail.com](mailto:test@gmail.com)",

# "password": "1234"

# }

#

# What happens:

# → Password is hashed

# → Stored in DB

# 2️⃣ LOGIN

# -----------------

# API: POST /login

# Body:

# {

# "email": "[test@gmail.com](mailto:test@gmail.com)",

# "password": "1234"

# }

#

# What happens:

# → Check email exists

# → Check password correct

# → Generate JWT token

#

# Output:

# {

# "access_token": "abc123..."

# }

# 3️⃣ COPY TOKEN

# -----------------

# Copy the access_token from login response

# 4️⃣ CALL SECURE API

# -----------------

# API: GET /secure

#

# In Postman → Headers:

# Key: Authorization

# Value: Bearer <paste_token_here>

#

# Example:

# Authorization: Bearer eyJhbGciOiJIUzI1Ni...

# 5️⃣ WHAT SERVER DOES

# -----------------

# → Read token from header

# → Decode token

# → Get email from token

# → If valid → allow

# → If invalid → 401 error

# =========================

# 🧪 TEST STEPS (POSTMAN)

# =========================

# Step 1:

# POST http://localhost:8000/register

# Step 2:

# POST http://localhost:8000/login

# → Copy token

# Step 3:

# GET http://localhost:8000/secure

# → Add Header:

# Authorization: Bearer <token>

# ✅ If correct → success

# ❌ If wrong/expired → 401

# =========================

# 🧠 ONE LINE MEMORY

# =========================

# Login → get token → send token → access secure API
