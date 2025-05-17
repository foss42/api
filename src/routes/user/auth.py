from fastapi import APIRouter, Depends, Response
from datetime import timedelta

from fastapi.security import OAuth2PasswordBearer

from models.user.auth import TokenResponseModel, UserLoginModel
from models.responses import ok_200, internal_error_500
from foss42.user.config import ACCESS_TOKEN_EXPIRE_MINUTES, COOKIE_NAME
from foss42.user.auth import create_access_token


auth_router = APIRouter(tags=["User Authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login", auto_error=False)


@auth_router.post("/login")
async def login_for_access_token(response: Response, data: UserLoginModel = Depends()):
    try:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": data.username}
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
