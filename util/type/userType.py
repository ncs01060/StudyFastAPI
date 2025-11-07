from typing import Optional
from pydantic import BaseModel
class User(BaseModel):
    name:str
    password:str
    createPage:Optional[int] = 0