from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from database import login_collection

app = FastAPI()

# allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/login")
async def login(
    username: str = Form(...),
    password: str = Form(...)
):

    data = {
        "username": username,
        "password": password  # (demo only)
    }

    result = await login_collection.insert_one(data)

    return {
        "success": True,
        "id": str(result.inserted_id)
    }