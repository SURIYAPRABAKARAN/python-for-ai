from fastapi import FastAPI
from controller import user_controller,product_controller

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(product_controller.router)

@app.get("/")
def root():
    return {"message": "Server is running! Try /users/suriya"}