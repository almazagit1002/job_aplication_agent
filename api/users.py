from fastapi import APIRouter, HTTPException
from typing import List

from .utils.users import get_user_by_email, get_user_by_id
from db.models.user import User
from db.db_set_up import user_collection

router = APIRouter()


# Create User
@router.post("/users/", response_model=User)
async def create_user(user: User):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_dict = user.dict(by_alias=True)
    user_dict["_id"] = str(user.id)  # Ensure id is stored as a string
    
    result = await user_collection.insert_one(user_dict)
    user.id = str(result.inserted_id)  # Convert inserted_id to string
    return user

# Read User
@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: str):
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# List Users
@router.get("/users/", response_model=List[User])
async def list_users(skip: int = 0, limit: int = 10):
    cursor = user_collection.find().skip(skip).limit(limit)
    users = await cursor.to_list(length=limit)
    for user in users:
        user["_id"] = str(user["_id"])  # Convert _id to string
    return [User(**user) for user in users]

# Update User
@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: str, user: User):
    update_result = await user_collection.update_one(
        {"_id": user_id},
        {"$set": user.dict(exclude_unset=True, by_alias=True, exclude={"created_at"})}
    )
    
    if update_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = await get_user_by_id(user_id)
    return updated_user

# Delete User
@router.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: str):
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    await user_collection.delete_one({"_id": user_id})
    return user
