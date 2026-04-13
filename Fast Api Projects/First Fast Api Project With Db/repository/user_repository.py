from db.database import SessionLocal
from db.models import UserDetails
from sqlalchemy import or_

def create_user_repo(user):
    db = SessionLocal()
    new_user = UserDetails(
        name=user.name,
        age=user.age,
        email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return new_user

def get_all_users():
    db = SessionLocal()
    users = db.query(UserDetails).all()
    db.close()
    return users

def get_user_by_id(user_id : int):
    db = SessionLocal()
    user = db.query(UserDetails).filter(UserDetails.id == user_id).first()
    db.close()
    return user

def delete_user_by_id(user_id : int):
    db = SessionLocal()
    user = db.query(UserDetails).filter(UserDetails.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        db.close()
        return True
    else:
        return False
    
def update_user(user_data):
    db = SessionLocal()
    try:
        # 1. Use or_() for the filter condition
        user = db.query(UserDetails).filter(
            or_(UserDetails.id == user_data.id, UserDetails.name == user_data.name)
        ).first()

        if user is None:
            raise Exception("User Not Found")

        # 2. Update the existing object attributes
        user.name = user_data.name
        user.age = user_data.age
        user.email = user_data.email

        db.commit()
        db.refresh(user)
        return user
    finally:
        db.close()