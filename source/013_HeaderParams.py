import uvicorn
from fastapi import FastAPI, Header

app = FastAPI(debug = True)


@app.get("/items/")
async def read_items(*, ads_id: str = Header("abc")):
    return {"ads_id": ads_id}


@app.get("/itemsOne/")
async def read_items(*, user_agent: str = Header(None)):
    return {"User-Agent": user_agent}


@app.get("/itemsTwo/")
async def read_items(*, strange_header: str = Header(None, convert_underscores=False)):
    return {"strange_header": strange_header}


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)