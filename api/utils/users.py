from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from db.models.user import User, Role
from db.db_set_up import users_collection
from bson import ObjectId

app = FastAPI()

# # Helper functions
# async def get_user_by_email(email: str):
#     user_doc = await users_collection.find_one({"email": email})
#     if user_doc:
#         return User(**user_doc)
#     return None

# async def get_user_by_id(user_id: str):
#     user_doc = await users_collection.find_one({"_id": ObjectId(user_id)})
#     if user_doc:
#         return User(**user_doc)
#     return None

# Create User
@app.post("/users/", response_model=User)
async def create_user(user: User):
    # existing_user = await get_user_by_email(user.email)
    # if existing_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    
    result = await users_collection.insert_one(user.dict(by_alias=True))
    user.id = result.inserted_id
    return user

# Read User
# @app.get("/users/{user_id}", response_model=User)
# async def read_user(user_id: str):
#     user = await get_user_by_id(user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# # List Users
# @app.get("/users/", response_model=List[User])
# async def list_users(skip: int = 0, limit: int = 10):
#     cursor = users_collection.find().skip(skip).limit(limit)
#     users = await cursor.to_list(length=limit)
#     return [User(**user) for user in users]

# # Update User
# @app.put("/users/{user_id}", response_model=User)
# async def update_user(user_id: str, user: User):
#     result = await users_collection.update_one(
#         {"_id": ObjectId(user_id)},
#         {"$set": user.dict(exclude_unset=True, by_alias=True, exclude={"created_at"})}
#     )
#     if result.modified_count == 0:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     updated_user = await get_user_by_id(user_id)
#     return updated_user

# # Delete User
# @app.delete("/users/{user_id}", response_model=User)
# async def delete_user(user_id: str):
#     user = await get_user_by_id(user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     await users_collection.delete_one({"_id": ObjectId(user_id)})
#     return user
