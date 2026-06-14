from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

if not MONGO_URL:
    raise Exception("MONGO_URL missing in .env")

client = AsyncIOMotorClient(MONGO_URL)

db = client.discord_clone
login_collection = db.login_attempts