from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()

itemLst = []

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.post("/AddJSON")
def post_item(item: Item):
    itemLst.append(item)

@app.get("/GetJSON")
def get_items():
    return itemLst


if __name__ == '__main__':
    uvicorn.run(app)
