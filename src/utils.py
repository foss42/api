from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import Cookie, Depends
from jose import JWTError, jwt
from config import ALGORITHM, COOKIE_NAME, SECRET_KEY
from models.responses import unauthorized_401
from models.user.auth import TokenData
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login", auto_error=False)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(
    token: Optional[str] = Depends(oauth2_scheme),
    access_token: Optional[str] = Cookie(None, alias=COOKIE_NAME)
):
    credentials_exception = unauthorized_401("Could not validate credentials")
    jwt_token = token or access_token

    if jwt_token is None:
        raise credentials_exception
    try:
        payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    return token_data
