from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from http import HTTPStatus
from typing import Optional, Any


def bad_request_400(msg: Optional[str] = None) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=HTTPStatus.BAD_REQUEST(1) if msg is None else msg,
    )


def not_found_404(msg: Optional[str] = None) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=HTTPStatus.NOT_FOUND(1) if msg is None else msg,
    )


def internal_error_500(msg: Optional[str] = None) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=HTTPStatus.INTERNAL_SERVER_ERROR(1) if msg is None else msg,
    )


def ok_200(data: Any = None) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"data": data}
    )
