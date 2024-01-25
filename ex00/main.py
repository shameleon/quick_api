import uvicorn

"""
from a web browser, open local page `127.0.0.1:8000`:

`localhost:8000/docs` to open requests
"""


if __name__ == "__main__":
    uvicorn.run("app.app:app",
                host="127.0.0.1",
                port=8000,
                reload=True)