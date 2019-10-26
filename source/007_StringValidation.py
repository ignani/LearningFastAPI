import uvicorn
from fastapi import FastAPI, Query
from typing import List

app = FastAPI(debug = True)

# Using min & max length, and reqular expressions for validating a string
# @app.get("/items/")
# async def get_items(item_id: str = Query(..., min_length = 2, max_length = 10, regex="^Item\d{1,6}")):
#     return {"item": item_id}
#
#
# # Valid
# @app.get("/items/")
# async def get_items(item_id: List[str] = Query(["Pen", "Pencil"], min_length = 2, max_length = 10)):
#     results = {"items": item_id}
#     return results
#
#
# # Adding metadata to parameters
# @app.get("/items/")
# async def get_items(item_id: List[str] = Query(["Pen", "Pencil"], min_length = 2, max_length = 10)):
#     results = {"items": item_id}
#     return results
#
#
# # Deprecating parameters
# @app.get("/items/")
# async def get_items(item_id: List[str] = Query(["Pen", "Pencil"], title = "Item List",
#                                                description = "List of items to be returned.",
#                                                min_length = 2, max_length = 10, deprecated = True)):
#     results = {"items": item_id}
#     return results


# Alias parameters
@app.get("/items/")
async def get_items(item_id: List[str] = Query(["Pen", "Pencil"], title = "Item List",
                                               description = "List of items to be returned.",
                                               min_length = 2, max_length = 10, deprecated = True, alias = "item-id")):
    results = {"items": item_id}
    return results


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)

item_id: str = None