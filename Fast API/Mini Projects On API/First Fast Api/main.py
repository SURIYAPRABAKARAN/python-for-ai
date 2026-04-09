from fastapi import FastAPI
import math
from service import user_service

app = FastAPI()

# get end point

@app.get("/hello")
def getAll():
    return user_service.get_all()
    
@app.get("/with_name/{name}")
def get_with_name(name : str):
    return user_service.get_with_name(name)

@app.get("/squre/{number}")
def get_squre_for_given_number(number:int):
    return user_service.calculate_square(number);