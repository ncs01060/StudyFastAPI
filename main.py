from typing import Union
from fastapi import FastAPI
import util.type as mainType
from util.storeAPI import userDataBase

app = FastAPI()

init = userDataBase()
init.initDB()


@app.get("/")
def read_root():

    return {"Hello":"World"}


@app.post("/sigup/")
def saveUserData(data:mainType.User):
    db = userDataBase()
    return db.saveData(data.name,data.password)

@app.post("/login/")
def userLogin(data:mainType.User):
    db = userDataBase()
    return db.login(data.name,data.password)

# python3 -m uvicorn main:app --reload --port 5050