from typing import Union
import httpx as htp
from fastapi import FastAPI, Request

app = FastAPI()
database = {}


# @app.get("/")
# def read_root():
#     return {"Hello": "1"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, txt: Union[str, None] = None):
#     database[item_id] = txt
#     return True if item_id in database else False

# @app.get("/items/")
# def read_database():
#     return database

@app.get("/search/")
def headers(request: Request, query):
    pars = htp.get(f'https://steamcommunity.com/market/search/render/?query={query}&norender=1', timeout=30)
    b = pars.json()
    return {'content': b}