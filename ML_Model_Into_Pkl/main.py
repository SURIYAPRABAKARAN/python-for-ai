import pickle
from pydantic import BaseModel
from fastapi import FastAPI

with open('model.pkl','rb') as f:
    model = pickle.load(f)
    

class PredictionRequest(BaseModel):
    age: int
    salary: int
    
app = FastAPI()

@app.post("/predict")
def predict(data: PredictionRequest):

    input_data = [[data.age, data.salary]]

    prediction = model.predict(input_data)

    result = "Will Buy" if prediction[0] == 1 else "Will Not Buy"

    return {"prediction": result}