from fastapi import HTTPException, status
from models.settings import const

ex_invalid = HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = const.msg_invalid_input,
        )
