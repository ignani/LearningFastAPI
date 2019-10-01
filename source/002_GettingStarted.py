import uvicorn
from fastapi import FastAPI

app = FastAPI(debug = True)


# A simple hello world api. It uses the get method. / indicates the root, however this doesn't have any reason why the method is named root.
# The method name can be anything.
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/home")
async def myhome():
    return {"message": "Home Page"}

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)