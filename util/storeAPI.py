import sqlite3
import uuid
import logging
import hashlib

class userDataBase:
    def __init__(self):
        self.userdb = sqlite3.connect("./util/db/userData.db")
        self.logger = logging.getLogger("util.storeAPI")
        self.logger.setLevel(logging.INFO)


        file_handler = logging.FileHandler("log/user.log", encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        ))



        if not self.logger.handlers:
            self.logger.addHandler(file_handler)


    def initDB(self):
        cur = self.userdb.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS User(id INTEGER PRIMARY KEY AUTOINCREMENT,Name text,password text, CreatePage number, uuid text);")
    
    def saveData(self,name:str,pwd:str):
        user_uuid = uuid.uuid4()
        cur = self.userdb.cursor()
        cur.execute("INSERT INTO User (Name, password, CreatePage, uuid) VALUES (?, ?, ?, ?)", (name,hashlib.sha256(pwd.encode()).hexdigest(), 0, str(user_uuid)))
        self.userdb.commit()
        self.logger.info(f"User saved: {name}, UUID: {user_uuid}")
        return {True}
    

    def login(self,name:str,pwd:str):
        
        cur = self.userdb.cursor()
        cur.execute("SELECT uuid FROM User WHERE name=? AND password=?;", (name, hashlib.sha256(pwd.encode()).hexdigest()))

        result = cur.fetchone()
        
        if result:
            self.logger.info(f"User '{name}' logged in with UUID {list(result)[0]}")
            return {"success": True, "uuid": list(result)[0]}
        else:
            self.logger.error(f"Login failed for user: {name}")
            return{"ERROR:404":"undefind"}

