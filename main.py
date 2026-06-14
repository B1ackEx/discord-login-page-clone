from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from database import login_collection

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def home():
    return FileResponse("static/index.html")


@app.post("/login")
async def login(
    username: str = Form(...),
    password: str = Form(...)
):
    login_data = {
        "username": username,
        "password": password
    }

    result = await login_collection.insert_one(login_data)

    return {
        "success": True,
        "id": str(result.inserted_id)
    }