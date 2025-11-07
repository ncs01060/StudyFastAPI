from typing import Union,Optional
from fastapi import FastAPI,Header
import util.type as mainType
from util.storeAPI import userDataBase

app = FastAPI()

init = userDataBase()
init.initDB()


@app.get("/")
def read_root():

    return {"Hello":"World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id:int, item:mainType.Item):
    return {"itemName":item.name , "item_id":item_id}


@app.post("/sigup/")
def saveUserData(data:mainType.User):
    db = userDataBase()
    return db.saveData(data.name,data.password)

# python3 -m uvicorn main:app --reload --port 5050