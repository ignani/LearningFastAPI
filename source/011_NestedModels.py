import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Set, Dict

app = FastAPI(debug = True)


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str = Field(None, title="Description of the item", max_length=250)
    price: float = Field(..., gt=0, le=100, description="The price must be greater than zero and lesser than or equal to 100")
    tax: float = None
    tags: Set[str] = []
    images: List[Image] = None


class Offer(BaseModel):
    name: str
    description: str = None
    price: float
    items: List[Item]


@app.put("/items/{item_id}")
async def update_item(*, item_id: int, offers: List[Offer]):
    results = {"item_id": item_id, "Offer": offers}
    return results


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)
