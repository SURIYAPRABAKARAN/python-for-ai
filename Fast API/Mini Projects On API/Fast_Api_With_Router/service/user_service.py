from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from model.user_model import User

def get_users(username):
    print(f"username from user crtl : {username}")
    return {
        "names" : ["suriya","sachin"],
        "age" : [25,55],
        "fav_sports" : [["cricket","badmintion"],["cricket","golf"]]
    }
    

    
def get_user_details(user : User):
        return {
        "message": "User created successfully",
        "data": user
    }