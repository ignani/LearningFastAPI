from enum import Enum

import uvicorn
from fastapi import FastAPI

# Example demonstrating accepting only pre-defined values as the parameter value using python Enum.
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
app = FastAPI()


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.lenet.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


# Sample demonstrating the file path as the parameter value
@app.get("/files/{file_path:path}")
async def read_user_me(file_path: str):
    return {"file_path": file_path}

# url/files//myfolder/file.txt
# Example of Path Parameter demonstrating
# - passing simple parameters
# - passing parameters with predefined types
# - importance of ordering the path and parameters
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}
#
#
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)