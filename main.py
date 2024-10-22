from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()
list = []


class Item(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/upMsg")
async def upMsg(item: Item):
    list.append(item.msg)
    return {"message": "success"}


@app.get("/getMsg")
async def get_msg():
    if list.__len__() != 0:
        return {"message": "success", "data": list.pop(0)}
    else:
        return {"message": "No message in the list"}


def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run()
