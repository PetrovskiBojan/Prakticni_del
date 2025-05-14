from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a model for the POST request body
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

# GET endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

# POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {"received_item": item}
