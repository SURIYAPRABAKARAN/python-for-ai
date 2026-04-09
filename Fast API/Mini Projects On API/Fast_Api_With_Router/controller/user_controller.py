from fastapi import APIRouter
from service import user_service
from service.user_service import User
from model.user_model import UserResponse


router = APIRouter(prefix="/users")

@router.get("/{username}")
def get_users(username:str):
    users = user_service.get_users(username)
    print(f"length {len(users)}")
    return users


@router.post("/user_details",response_model=UserResponse)
def get_user_details(user:User):
    return user_service.get_user_details(user)