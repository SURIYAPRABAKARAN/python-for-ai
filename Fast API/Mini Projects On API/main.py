from fastapi import FastAPI
import math

app = FastAPI()

# get end point

@app.get("/hello")
def getAll():
    return {"name":"suriya",
            "age" : 25,
            "skills" : ["Java","python","ML"]}
    
@app.get("/with_name/{name}")
def get_with_name(name : str):
    return {"user": name}

@app.get("/squre/{number}")
def get_squre_for_given_number(number:int):
    # return math.sqrt(number)
    return number * number;