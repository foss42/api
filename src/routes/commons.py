from fastapi import HTTPException, status
from models.settings import const

EX_INVALID = HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = const.msg_invalid_input,
        )

def custom_exception(msg: str):
    return HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = msg,
        )