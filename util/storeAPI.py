import sqlite3

class userDataBase:
    def __init__(self):
        self.textdb = sqlite3.connect("./util/db/userText.db")
        self.userdb = sqlite3.connect("./util/db/userData.db")

    def initDB(self):
        cur = self.userdb.cursor()
        cur.execute("CREATE TABLE User(id INTEGER PRIMARY KEY AUTOINCREMENT,Name text, CreatePage number);")
    
    def saveData(self,name:str):
        cur = self.userdb.cursor()
        cur.execute("INSERT INTO User (Name, CreatePage) VALUES (?, ?)", (name, 0))
        self.userdb.commit()
        return {True}

