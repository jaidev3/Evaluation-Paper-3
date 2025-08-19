
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "https://localhost:5173",
    "http://localhost:3000",
    "http://localhost:8080",
]

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
