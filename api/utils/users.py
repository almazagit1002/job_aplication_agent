from db.models.user import User
from db.db_set_up import user_collection



# Helper functions
async def get_user_by_email(email: str):
    user_doc = await user_collection.find_one({"email": email})
    if user_doc:
        user_doc["_id"] = str(user_doc["_id"])  # Convert _id to string
        return User(**user_doc)
    return None

async def get_user_by_id(user_id: str):
    user_doc = await user_collection.find_one({"_id": user_id})
    if user_doc:
        return User(**user_doc)
    return None
