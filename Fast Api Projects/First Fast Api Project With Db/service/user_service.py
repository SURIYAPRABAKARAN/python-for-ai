from repository.user_repository import create_user_repo

def create_user_service(user):
    return create_user_repo(user)