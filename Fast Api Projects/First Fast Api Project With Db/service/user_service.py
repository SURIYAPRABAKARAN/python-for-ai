from repository.user_repository import create_user_repo , get_all_users , get_user_by_id , delete_user_by_id

def create_user_service(user):
    return create_user_repo(user)

def get_all_users_service():
    return get_all_users()

def get_user_by_id_service(user_id : int):
    return get_user_by_id(user_id)

def delete_user_by_id_service(user_id : int):
    return delete_user_by_id(user_id)