import uvicorn
from fastapi import FastAPI, Query, Path

app = FastAPI(debug = True)

@app.get("/items/")
async def read_items(item_id: str = Query(..., min_length = 2, max_length = 10, regex="^Item\d{1,6}")):
    results = {"items": [{"item_id": "Pen"}, {"item_id": "Pencil"}]}
    results.update({"New Item": item_id})
    return {"item": item_id}

# @app.get("/items/{item_id}")
# async def read_items(item: str, item_id: str = Path(...,description = "Item id")):
#     return {"item_id": item_id, "item": item}


# Basic Number Validation
# @app.get("/items/{item_id}")
# async def read_items(item: str,
#                      item_id: float = Path(...,description = "Item id")):
#     return {"item_id": item_id, "item": item}


# Max & Minimum number validation
@app.get("/items/{item_id}")
async def read_items(item: int = Query(None, gt = 1, le = 100),
                     item_id: float = Path(...,description = "Item id", ge = 1, le = 10,)):
    return {"item_id": item_id, "item": item}


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)

item_id: str = None