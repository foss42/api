from fastapi import APIRouter, Depends
from foss42.user.users import get_random_user_data, get_all_users_data, get_user_data_by_id
from models.responses import not_found_404, internal_error_500, unauthorized_401
from models.user.user_data import UserListResponseModel, UserModel
from routes.user.auth import oauth2_scheme

user_data_router = APIRouter(tags=["User Data"])

@user_data_router.get("/profile")
async def read_random_profile(token: str = Depends(oauth2_scheme)):
    
    if token is None:
        raise unauthorized_401("Not authenticated")
    
    try:
        random_user_data = get_random_user_data()
        if not random_user_data:
            raise not_found_404("No users available")
        user = UserModel(**random_user_data)
        return user
    except Exception as e:
        print(e)
        raise internal_error_500("Could not fetch profile")


@user_data_router.get("/users", response_model = UserListResponseModel)
async def read_all_users():
    try:
        users_list = get_all_users_data()
        users = [UserModel(**user_data) for user_data in users_list]
        return UserListResponseModel(data=users)
    except Exception as e:
        raise internal_error_500("Could not fetch users")


@user_data_router.get("/users/{user_id}", response_model = UserModel)
async def read_user_by_id(user_id: int):
    try:
        user_data = get_user_data_by_id(user_id)
        if not user_data:
            raise not_found_404(f"No user with id {user_id} found")
        user = UserModel(**user_data)
        return user 
    except Exception as e:
        raise internal_error_500("Could not fetch user")
