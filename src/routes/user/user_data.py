from fastapi import APIRouter, Depends
import random
from const import USERS
from models.responses import ok_200, not_found_404, internal_error_500
from models.user.user_data import UserListResponseModel, UserModel
from .auth import get_current_active_user, TokenData

user_data_router = APIRouter(tags=["User Data"])

@user_data_router.get("/profile")
async def read_users_me(current_user: TokenData = Depends(get_current_active_user)):
    try:
        if not USERS:
            raise not_found_404("No users available")
        random_user_data = random.choice(USERS)
        user = UserModel(**random_user_data)
        return user
    except Exception as e:
        raise internal_error_500("Could not fetch profile")


@user_data_router.get("/users", response_model = UserListResponseModel)
async def read_all_users():
    try:
        users = [UserModel(**user_data) for user_data in USERS]
        return UserListResponseModel(data=users)
    except Exception as e:
        raise internal_error_500("Could not fetch users")


@user_data_router.get("/users/{user_id}", response_model = UserModel)
async def read_user_by_id(user_id: int):
    try:
        if user_id < 1 or user_id > len(USERS):
             raise not_found_404(f"User with ID {user_id} not found")
        user_data = USERS[user_id - 1]
        user = UserModel(**user_data)
        return user
    except Exception as e:
        raise internal_error_500("Could not fetch user")