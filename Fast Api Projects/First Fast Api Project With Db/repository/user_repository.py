from db.database import SessionLocal
from db.models import UserDetails

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