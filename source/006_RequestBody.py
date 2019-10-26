import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(debug = True)


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        total = item.price + item.tax
        item_dict.update({"TotalAmount" : total})
    return item_dict


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)
