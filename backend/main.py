
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, PositiveInt
from typing import List, Annotated
from datetime import date
# from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


# db = create_engine("sqlite:///smartfit.db", echo=True)

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

origins = [
    "http://localhost",
    "https://localhost:5173",
    "http://localhost:3000",
    "http://localhost:8080",
]


# Schemas
class User(SQLModel):
    id: int
    username: str
    email: EmailStr
    password: str
    # age: PositiveInt
    # weight: PositiveInt
    # height: PositiveInt
    # goal: List[str]

class Workout(BaseModel):
    id: int
    user_id: int
    plan_name: str
    date: date
    expercises: List[str]
    duration: int

class Nutrition(BaseModel):
    id: int
    user_id: int
    date: date
    meals: List[str]
    calories: int
    macros: int

class Progress(BaseModel):
    id: int
    user_id: int 
    workout_id: int
    sets: int
    reps: int
    weights: int
    notes: str

class Exercise(BaseModel):
    id: int
    user_id: int
    exercise_name: str
    category: str
    equipment_needed: List[str]
    difficulty: str
    instructions: List[str]
    target_muscles: str


# import uvicorn
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Authentication 
@app.get("/health")
async def root():
    return {"message": "OK"}

@app.post("/auth/register")
async def register(user: User, session: SessionDep):
    session.add(user)
    # session.commit()
    # session.refresh(user)
    # return user
    return {"message": user}

@app.post("/auth/login")
async def login():
    return {"message": "Login"}

@app.get("auth/user/{user_id}")
async def profile():
    return {"message": "Profile"}


# Core CRUD
# GET/POST/PUT/DELETE /workouts - Workout management
# GET/POST/PUT/DELETE /exercises - Exercise database
# GET/POST/PUT/DELETE /nutrition - Nutrition logging
# GET/POST/PUT/DELETE /progress - Progress tracking
# AI Chat
# POST /chat/ask - Send question, get RAG-powered response
# GET /chat/history/{user_id} - Get chat history

@app.post("/workout")
def add_workout():
    return {"message": "workout added"}

@app.get("/workout")
def get_all_workout():
    return {"message": "All workout"}

@app.get("/workout/{workout_id}")
def get_workout():
    return {"message": "workout get"}

@app.put("/workout/{workout_id}")
def put_workout():
    return {"message": "workout edited"}

@app.delete("/workout/{workout_id}")
def delete_workout():
    return {"message": "workout deleted"}




# if __name__ == "__main__":
#     uvicorn main:app --host 0.0.0.0 --port 8080
