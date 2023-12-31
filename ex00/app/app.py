from fastapi import FastAPI

app = FastAPI()

# minimal app GET request
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Ping" : "Pong"}


# GET --> Read todo
@app.get("/todo", tags=["todos"])
async def get_todo() -> dict:
    return {"data": todos}

# POST -> Create todo
@app.post("/todo", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {"data": "a todo has been added"}

# PUT --> Update todo
@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todo['activity'] = body['activity']
            return {"data": f'todo #{id} has been updated'}
    return {"data": f'todo #{id} was not found !'}

# DELETE -> delete todo
@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todos.remove(todo)
            return {"data": f'todo #{id} has been deleted'}
    return {"data": f'todo #{id} was not found !'}

todos = [
{
    "id": "1",
    "activity": "Jogging in the pak at 1:00 PM."
},
{
    "id": "2",
    "activity": "Writting 3 pages of my novel at 2:00 PM."
}
]