from fastapi import APIRouter
from model.user_model import User
from service.user_service import create_user_service

router = APIRouter(prefix="/users")

@router.post("/")
def create_user(user: User):
    create_user_service(user)