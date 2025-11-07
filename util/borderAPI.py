import sqlite3
import logging
import util.type as baseType
import uuid
class BorderAPI:
    def __init__(self):
        self.borderDB = sqlite3.connect("./util/db/userText.db")
        self.logger = logging.getLogger("util.borderAPI")
        self.logger.setLevel(logging.INFO)


        file_handler = logging.FileHandler("log/border.log", encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        ))



        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
    
    def initDB(self):
        cur = self.borderDB.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Board(id INTEGER PRIMARY KEY AUTOINCREMENT," \
        "title text," \
        " Created text, " \
        "uuid text," \
        "author text," \
        "viwer number," \
        "mainText text," \
        "borderUID text);")

        cur.execute("CREATE TABLE IF NOT EXISTS Likes (id INTEGER PRIMARY KEY AUTOINCREMENT," \
        "userUUID TEXT," \
        "borderUID TEXT," \
        "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP," \
        "UNIQUE(userUUID, borderUID));")
    
    def writeBorder(self, data:baseType.BorderType):
        cur = self.borderDB.cursor()
        border_uuid = str(uuid.uuid4())
        cur.execute("INSERT INTO Board (title, Created, uuid, author, viwer, mainText, borderUID) VALUES (?, ?, ?, ?, ?, ?, ?)",(data.title, data.created, data.uid, data.author, data.viewer, data.text, border_uuid))

        self.borderDB.commit()
        self.logger.info(f"{border_uuid} 게시글이 생겼습니다.")
        return {True}
    
    def deleteBorder(self,uuid:str):
        cur = self.borderDB.cursor()
        cur.execute("DELETE FROM Board WHERE borderUID = ?",(uuid,))
        self.borderDB.commit()
        self.logger.info(f"{uuid} 게시글이 삭제되었습니다.")
        return {True}
    
    def addLike(self, user_uuid: str, border_uid: str):
        cur = self.borderDB.cursor()
        try:
            cur.execute("INSERT INTO Likes (userUUID, borderUID) VALUES (?, ?)", (user_uuid, border_uid))
            self.borderDB.commit()
            self.logger.info(f"{user_uuid} liked {border_uid}")
            return {"success": True}
        except sqlite3.IntegrityError:
            # 이미 좋아요를 누른 경우
            cur.execute("DELETE FROM Likes WHERE userUUID=? AND borderUID=?", (user_uuid, border_uid))
            self.borderDB.commit()
            self.logger.info(f"{user_uuid} unliked {border_uid}")
            return {"success": False, "message": "unliked"}
        
    def addLikeCheck(self,user_uuid:str, border_uid:str):
        cur = self.borderDB.cursor()
        cur.execute("SELECT ? FROM Likes WHERE borderUID=?",(user_uuid, border_uid,))
        result = cur.fetchone()
        if result:
            return True
        else:
            return False
    
    def getLikeCount(self, border_uid: str):
        cur = self.borderDB.cursor()
        cur.execute("SELECT COUNT(*) FROM Likes WHERE borderUID=?", (border_uid,))
        count = cur.fetchone()[0]
        return count