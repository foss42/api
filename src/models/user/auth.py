from pydantic import BaseModel
from typing import Optional

class UserLoginModel(BaseModel):
    username: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "jhon",
		        "password": "jhoniscool",
            }
        }

class TokenResponseModel(BaseModel):
    access_token: str
    token_type: str = "bearer"

    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "access_token",
		        "token_type": "bearer",
            }
        }

class TokenData(BaseModel):
    username: Optional[str] = None
