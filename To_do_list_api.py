from fastapi import FastAPI

app = FastAPI()

items = []
@app.get("/")
def root():
    return {"message": "Hello There"}

@app.post("/items/")
def add_item(item: str):
    items.append(item)
    return {"item": item}

@app.get("/items/")
def list_items():
    return {"items": items}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = items[item_id]
    return {"item_id": item_id, "item": item}