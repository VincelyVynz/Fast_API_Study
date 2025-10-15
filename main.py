from fastapi import FastAPI, HTTPException

app = FastAPI()


items = []
@app.get('/')
def root():
    return "Hello"

@app.post('/items')
def post_items(item:str):
    items.append(item)
    return items

@app.get('/items')
def get_items():
    return items