
# Quick-api
I am learning to use `FastAPI` python framework.
For that purpose, I am following tutorials buiding basic `API`'s using `FastAPI`.

## Summary

- [FastAPI](#FastAPI)
    - [Install](#Install)
    - [Ex00-basic CRUD with FastAPI](#ex00-basic-CRUD)
    - [Ex01-recipes using pydantic](#ex01-recipes)
    - [Ex02-users](#ex02-users)
- [Bottle](#Bottle)
    - [Glossary](#Glossary)

## FastAPI

[FastAPI docs](https://fastapi.tiangolo.com/)

[FastAPI’s Performance](https://christophergs.com/python/2021/06/16/python-flask-fastapi/)

FastAPI is built on top of Starlette, an ASGI (Asynchronous Server Gateway Interface) framework.

As `Flask`, `FastAPI` use decorators to mark `endpoints`.

For FastAPI, the recommended choice for an ASGI web server : `uvicorn`.

`Pydantic` is a library for data validation, Defining API config
and API requests/responses (JSON schemas).

`SwaggerUI` for documentation UI display.

### Install

from a *virtual environement* setup:

```shell
➜ virtualenv venv
➜ source venv/bin/activate
(venv)➜ pip install uvicorn fastapi
(venv)➜ python main.py
```

### Swagger UI

Then from a web browser, open local page `127.0.0.1:8000`:

`localhost:8000/docs` to open requests

### Pydantic

Data validation and settings management using python type annotations.
[Fastapi : request body with pydantic](https://fastapi.tiangolo.com/tutorial/body/)

### ex00-basic-CRUD

Creating a first basic CRUD API from the following video
[FastAPI Crash Course 2021 For Beginners, Bek Brace channel](https://youtu.be/62pP9pfzNRs?si=W-1WD)

```python
from fastapi import FastAPI

app = FastAPI()

# GET --> Read todo
@app.get("/todo", tags=["todos"])

# POST -> Create todo
@app.post("/todo", tags=["todos"])

# PUT --> Update todo
@app.put("/todo/{id}", tags=["todos"])

# DELETE -> delete todo`
@app.delete("/todo/{id}", tags=["todos"])
```

### ex01-recipes

To declare a request body, you use Pydantic models with all their power and benefits.
[pydantic docs](https://docs.pydantic.dev/latest/)

[ChristopherGS The ultimate FastAPI tutorial](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-1-hello-world/)

[](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-4-pydantic-schemas/)

### ex02-users

[sql](https://fastapi.tiangolo.com/tutorial/sql-databases/)
[](https://www.youtube.com/watch?v=7D_0JTeaKWg)
[](https://www.youtube.com/watch?v=SORiTsvnU28)

## Bottle

Bottle is a fast, simple and lightweight WSGI micro web-framework for Python.

[Bottle](https://bottlepy.org/docs/dev/)

## References
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
