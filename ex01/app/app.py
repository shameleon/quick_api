from fastapi import FastAPI
from typing import Optional, Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# minimal app GET request
@app.get("/")
async def root() -> dict:
    return {"Hello" : "World"}

# GET --> Read todo
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# POST -> Create todo
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}