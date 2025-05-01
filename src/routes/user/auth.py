from fastapi import APIRouter, Depends, Response
from datetime import timedelta

from models.user.auth import TokenData, TokenResponseModel, UserLoginModel
from models.responses import ok_200, internal_error_500
from config import *
from utils import create_access_token, get_current_user


auth_router = APIRouter(tags=["User Authentication"])


@auth_router.post("/login")
async def login_for_access_token(response: Response, data: UserLoginModel = Depends()):
    try:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": data.username}, expires_delta=access_token_expires
        )
        response.set_cookie(
            key=COOKIE_NAME,
            value=access_token,
            httponly=True,
            max_age=access_token_expires.total_seconds(),
            expires=access_token_expires,
            samesite="lax",
            secure=True,
        )
        
        return TokenResponseModel(access_token=access_token)
    except Exception as e:
       
        raise internal_error_500("Login failed")


@auth_router.post("/logout")
async def logout(response: Response):
    try:
        response.delete_cookie(COOKIE_NAME, httponly=True, samesite="lax", secure=True)
        return ok_200({"message": "Successfully logged out"})
    except Exception as e:
        raise internal_error_500("Logout failed")


async def get_current_active_user(current_user: TokenData = Depends(get_current_user)):
    return current_user