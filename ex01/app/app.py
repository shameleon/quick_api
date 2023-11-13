from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Coord(BaseModel):
    lat: float
    lon: float
    zoom: Optional[int]

# minimal app GET request
@app.get("/")
async def root() -> dict:
    return {"Hello" : "World"}


# GET --> Read todo

@app.get("/positions/")
async def get_all_positions() -> dict:
    return {"positions": positions}

@app.get("/positions/{id}")
async def get_position(id: int) -> dict:
    return positions[id]

# POST -> Create todo
@app.post("/position/")
async def add_postion(coord: Coord) -> dict:
    positions.append(coord)
    return {"data": "Position has been added"}

positions = []