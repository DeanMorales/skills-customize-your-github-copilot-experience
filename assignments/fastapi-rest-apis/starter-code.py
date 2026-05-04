from typing import Dict, Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

items: Dict[int, Dict] = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = Query(None, title="Query string", max_length=50)):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    result = {"item_id": item_id, **items[item_id]}
    if q:
        result["query"] = q
    return result

@app.post("/items")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item.dict()
    return {"item_id": item_id, **items[item_id]}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item.dict()
    return {"item_id": item_id, **items[item_id]}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted = items.pop(item_id)
    return {"item_id": item_id, "deleted": deleted}
