from typing import Union
from fastapi import APIRouter
from application.test1.schemas import Item


test1_router = APIRouter(
    prefix='/test1',
    tags=['测试一'],
)


@test1_router.get("/root")
def hello_world():
    return {'Hell0': "World"}


@test1_router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@test1_router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
