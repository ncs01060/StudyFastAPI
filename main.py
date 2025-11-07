from typing import Union
from fastapi import FastAPI
import util.type as mainType
from util.storeAPI import userDataBase
from util.borderAPI import BorderAPI

app = FastAPI()

init = userDataBase()
init.initDB()
borderInit = BorderAPI()
borderInit.initDB()


@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.post("/sigup/", status_code=200)
def saveUserData(data:mainType.User):
    db = userDataBase()
    db.saveData(data.name,data.password)

@app.get("/login/", status_code=200)
def userLogin(data:mainType.User):
    db = userDataBase()
    return db.login(data.name,data.password)


@app.post("/writeBorder/",status_code=200)
def writeBorder(data:mainType.BorderType):
    db = BorderAPI()
    db.writeBorder(data)

@app.delete("/deleteBorder/",status_code=200)
def deleteBorder(uid:str):
    db = BorderAPI()
    db.deleteBorder(uid)

@app.get("/getLike/")
def getLike(uid:str):
    db = BorderAPI()
    return db.getLikeCount(uid)

@app.get("/addLike")
def addLike(user_uid:str, border_uid:str):
    db = BorderAPI()
    return db.addLike(user_uid,border_uid)

@app.get("/addLikeCheck/")
def addLikeCheck(user_uid:str,border_uid:str):
    db = BorderAPI()
    return db.addLikeCheck(user_uid,border_uid)

# python3 -m uvicorn main:app --reload --port 5050