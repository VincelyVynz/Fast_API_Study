from fastapi import FastAPI, HTTPException
from datetime import datetime
app = FastAPI()


items = []
@app.get('/')
def home():
    return {"msg": "Hello There!"}

@app.get('/greet/{name}')
def greet(name:str):
    return {'msg': f"Greetings {name}"}


@app.get('/time')
def tell_time():
    time_now = datetime.now()
    return {"Time": f"The time now is {time_now}"}


