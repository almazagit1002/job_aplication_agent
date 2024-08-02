import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import  ASCENDING

mongo_url = os.getenv('MONGO_URL', 'mongodb://localhost:27017')
client = AsyncIOMotorClient(mongo_url)
# client = AsyncIOMotorClient('localhost', 27017)
db = client['job_database']
user_collection = db["users"]
user_collection.create_index([("email", ASCENDING)], unique=True)