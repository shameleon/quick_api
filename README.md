
# Quick-api
I am learning to use `FastAPI` python framework.
For that purpose, I am following tutorials buiding basic `API`'s using `FastAPI`.

## Summary

- [FastAPI](#FastAPI)
    - [Install](#Install)
    - [Ex00 :  basic CRUD](#Tutorial_00:_basic-CRUD)
    - [Glossary](#Glossary)

## FastAPI

[FastAPI docs](https://fastapi.tiangolo.com/)
### Install

from a *virtual environement* setup:

```shell
➜ virtualenv venv
➜ source venv/bin/activate
(venv)➜ pip install uvicorn fastapi
(venv)➜ python main.py
```

Then from a web browser, open local page `127.0.0.1:8000`:

`localhost:8000/docs` to open requests

### Tutorial_00:_basic-CRUD

Creating a first basic CRUD API  :

[FastAPI Crash Course 2021 For Beginners, Bek Brace channel](https://youtu.be/62pP9pfzNRs?si=W-1WD)

```python
# GET --> Read todo
@app.get("/todo", tags=["todos"])

# POST -> Create todo
@app.post("/todo", tags=["todos"])

# PUT --> Update todo
@app.put("/todo/{id}", tags=["todos"])

# DELETE -> delete todo`
@app.delete("/todo/{id}", tags=["todos"])
```

[](https://www.youtube.com/watch?v=SORiTsvnU28)


### Glossary
||||
|---|---|---|
|API| application programming interface||
|HTTP request methods|||
|ASGI|Asynchronous Server Gateway Interface||
|REST|Representational State Transfer||

### HTTP request methods
||||
|---|---|---|
||||
||||
