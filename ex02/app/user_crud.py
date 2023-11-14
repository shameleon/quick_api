from fastapi import FastAPI
from ex01.app.user_class import User, Users

app = FastAPI()

# minimal app GET request
@app.get("/")
async def root() -> dict:
    return {"Hello" : "API for users entries"}

# GET --> Read todo
@app.get("/users/")
def read_all_users() -> dict:
    return {"users": users}

# GET --> Read todo
@app.get("/users/{user_id}")
def read_user_by_id(user_id: int) -> dict:
    for user in users:
        if user['id'] == user_id:
            return {"user": user}
    return {'users': f'user id #{user_id} was not found !'}

# POST -> Create todo
@app.post("/users/{user_id}")
async def add_user(user: dict) -> dict:
    user_id = user['id']
    users.append(user)
    return {'users': f'user id #{user_id} was added !'}

users = []