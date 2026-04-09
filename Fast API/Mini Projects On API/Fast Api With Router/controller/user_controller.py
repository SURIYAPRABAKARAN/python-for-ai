from fastapi import APIRouter
from service import user_service

router = APIRouter(prefix="/users")

@router.get("/{username}")
def get_users(username:str):
    users = user_service.get_users(username)
    print(f"length {len(users)}")
    return users