import uvicorn
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel

app = FastAPI(debug = True)


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class User(BaseModel):
    username: str
    full_name: str = None

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: str = None,
    item: Item = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

#
# @app.put("/items_new/{item_id}")
# async def update_item(*, item_id: int, item: Item, user: User, q: int = Body(...)):
#     results = {"item_id": item_id, "item": item, "user": user, "q" : q}
#     return results

#
# @app.put("/items_new/{item_id}")
# async def update_item(*, item_id: int, item: Item, user: User, q: int = Body(...), x:str):
#     results = {"item_id": item_id, "item": item, "user": user, "q" : q}
#     return results


@app.put("/items_new/{item_id}")
async def update_item(*, item_id: int, item: Item = Body(..., embed = True)):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)
