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