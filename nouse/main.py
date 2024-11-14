import json
from typing import Union

from fastapi import FastAPI, Query

from pydantic import BaseModel

app = FastAPI()

import requests


class Item(BaseModel):
    name: str
    desc: str | None = None
    price: float
    tax: float | None = None


# 请求体 + 路径参数
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

# 请求体 + 路径参数 + 查询参数
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@app.get("/items")
async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# printhsgshgsd
###sdjhsdjufgsdyfgsdprint

response = requests.post(url='http://localhost:8337/model/property/listByKeys', json={"projectId":"18c1foju-144-1zx","modelId":"81622159838481472","keys":["DiagramTable-scope"]})
# print(response.text)

# 数据格式化处理
json_show = json.dumps(response.json(), indent=2)
print(json_show)

###123



