from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Items(BaseModel):
    name:str 
    description:str | None=None
    price: float
    tax:float | None=None


@app.post('/items/')
def craete_item(item:Items):
    return item

from typing import Annotated
from fastapi import Query
# default value is none
# @app.get("/items/")
# async def read_items(q:Annotated[str|None,Query(min_length=10,max_length=50,regex='^fixedquery$')]=None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# # default value is hello world
# @app.get('/names')
# async def itemss(name:Annotated[str|None,Query(min_length=3,max_length=10,regex='^fixedquery$')]="hello world"):
#     return {"names":"firstname"}

# # value is required
# @app.get('world/{id}')
# async def item(id:Annotated[int,Query(min=1,max=10)]=None):
#     return id

# take multiple q strings
@app.get('/strs')
async def strs(q:Annotated[list[str]|None,Query()]=["firstname","lastname"]):
    return q


@app.get("/namess")
async def name(q:Annotated[str|None,Query(description="enter your name",title="name",max_length=10,include_in_schema=False)]=None):
    return q