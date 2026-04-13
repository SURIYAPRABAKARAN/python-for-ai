from fastapi import APIRouter
from model.user_model import User
from service.user_service import create_user_service , get_all_users_service , get_user_by_id_service , delete_user_by_id_service

router = APIRouter(prefix="/users")

@router.post("/")
def create_user(user: User):
    create_user_service(user)
    
@router.get("/all_users")
def get_all_users_controller():
    return get_all_users_service()

@router.get("/user_by_id/{user_id}")
def get_user_by_id_controller(user_id: int):
    return get_user_by_id_service(user_id)

@router.delete("/delete_user_by_id/{user_id}")
def delete_user_by_id(user_id : int):
    is_user_deleted = delete_user_by_id_service(user_id)
    if is_user_deleted:
        return {"Message": f"Given User Deleted Successfully : {user_id}"}
    else:
        return {"Message": f"Given User Not Found In The Data Base : {user_id}"}