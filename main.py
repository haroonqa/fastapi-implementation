from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI app
app = FastAPI()

# Part 2: Define the Item model
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Part 1: Create a root GET endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Part 1: Create a GET endpoint with path and query parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Part 2: Create a PUT endpoint to update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
