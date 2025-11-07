from typing import Union,Optional
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    price:float
    is_offer: Union[bool,None] = None
