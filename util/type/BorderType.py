from pydantic import BaseModel
from typing import Optional

class BorderType(BaseModel):
    title:str
    created:str
    author:str
    viewer: Optional[int] = 0
    text:str
    uid:str