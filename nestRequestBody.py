from typing import Optional
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


class ShopInfo(BaseModel):
    name:str
    location:str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax:Optional[float] = None

class Data(BaseModel):
    shop_info:Optional[ShopInfo] = None
    items:List[Item]



app = FastAPI()

@app.post("/")
async def index(data: Data):
    return {"data":data}




