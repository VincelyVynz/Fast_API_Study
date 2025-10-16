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
    time_now = datetime.now().strftime("%A, %B %d %Y, %I:%M %p")
    return {"Time": f"The time now is {time_now}"}


@app.get('/user/{user}/age/{age}')
def user_age(user:str, age:int):
    return {"msg": f"User {user} is {age} years old"}

@app.get('/weather/{city}')
def weather(city:str):
    city = city.title()
    return {'Weather report' : f'30 % chance for rain in {city}'}