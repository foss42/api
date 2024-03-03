import io
import time
import mimetypes
import puremagic
from typing import Annotated
from fastapi import (
    APIRouter,
    File,
    UploadFile,
    Form,
    Request
)
from models.responses import *
from fastapi.responses import Response
from foss42.text.slugify import slugify
import foss42.text.humanize as hz

io_router = APIRouter(tags=["I/O"])


@io_router.get('/delay')
async def delayed_request(wait: int = 5):
    try:
        if wait > 120:
            raise bad_request_400(msg="Delay cannot be more than 120 secs")
        time.sleep(wait)
        return ok_200(f"Waited for {wait} seconds")
    except Exception as e:
        raise internal_error_500()


@io_router.post('/form')
async def form_to_rotate_text_chars(text: Annotated[str, Form()],
                                    sep: Annotated[str, Form()],
                                    times: Annotated[int, Form()]):
    """
    text fields/text file attachment work for both
    application/x-www-form-urlencoded multipart/form-data
    """
    try:
        res = slugify(text,
                      sep)
        if times > 1:
            res = sep.join([res,]*times)
        return ok_200(res)
    except:
        raise internal_error_500()


@io_router.post("/filesize")
async def create_file(request: Request):
    try:
        content = await request.body()
        size = hz.humanize_bytes(len(content),
                                 2)
        header_content_type = dict(request.headers)["content-type"]
        stream = io.BytesIO(content)
        magic_conf = puremagic.magic_stream(stream)
        deduced_type = magic_conf[0].mime_type if len(magic_conf) > 0 else None
        return ok_200({"size": size,
                       "content-type": header_content_type,
                       "deduced-mime-type": deduced_type})
    except:
        raise internal_error_500()


@io_router.post('/echo_file')
async def echo_file(file: UploadFile):
    try:
        file_content = io.BytesIO(file.file.read()).getvalue()
        file_mimetype = mimetypes.guess_type(
            file.filename)[0] or "application/octet-stream"
        return Response(
            content=file_content,
            media_type=file_mimetype
        )
    except Exception as e:
        raise internal_error_500()
