import sqlite3
import uuid

class userDataBase:
    def __init__(self):
        self.textdb = sqlite3.connect("./util/db/userText.db")
        self.userdb = sqlite3.connect("./util/db/userData.db")

    def initDB(self):
        cur = self.userdb.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS User(id INTEGER PRIMARY KEY AUTOINCREMENT,Name text,password text, CreatePage number, uuid text);")
    
    def saveData(self,name:str,pwd:str):
        user_uuid = uuid.uuid4()
        cur = self.userdb.cursor()
        cur.execute("INSERT INTO User (Name, password, CreatePage, uuid) VALUES (?, ?, ?, ?)", (name,hash(pwd), 0, str(user_uuid)))
        self.userdb.commit()
        return {True}

