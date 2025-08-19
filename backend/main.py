
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, PositiveInt
from typing import List
from datetime import date

origins = [
    "http://localhost",
    "https://localhost:5173",
    "http://localhost:3000",
    "http://localhost:8080",
]


# Users: id, username, email, password, age, weight, height, goals
# Workouts: id, user_id, plan_name, date, exercises, duration
# Nutrition: id, user_id, date, meals, calories, macros
# Progress: id, user_id, workout_id, sets, reps, weights, notes
# Schemas
class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str
    age: PositiveInt
    weight: PositiveInt
    height: PositiveInt
    goal: List[str]

class Workout(BaseModel):
    id: int
    user_id: int
    plan_name: str
    date: date
    expercises: List[str]
    duration: int

# class Nut 



# import uvicorn
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/health")
async def root():
    return {"message": "OK"}

@app.post("/register")
async def register():
    return {"message": "Register"}

@app.post("/login")
async def login():
    return {"message": "Login"}

@app.get("/profile")
async def profile():
    return {"message": "Profile"}




# if __name__ == "__main__":
#     uvicorn main:app --host 0.0.0.0 --port 8080
