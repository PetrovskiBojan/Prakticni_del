from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# GET endpoint
@app.get("/")
def read_root():
    return {"message": "Prakticni del!"}

# POST endpoint
@app.post("/predict")
def create_item():
    return {"Get prediction"}
