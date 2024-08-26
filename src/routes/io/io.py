import io
import time
import puremagic
from typing import Annotated
from fastapi import (
    APIRouter,
    File,
    UploadFile,
    Form,
    Request,
    Resonse
)
from models.responses import *
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

@io_router.post('/img')
async def analyze_img_file(
    imfile: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    try:
        size = hz.humanize_bytes(imfile.size,
                                 2)
        magic_conf = puremagic.magic_stream(imfile.file)
        deduced_type = magic_conf[0].mime_type if len(magic_conf) > 0 else None
        return ok_200({
            "provided-token": token,
            "size": size,
            "content-type": imfile.content_type,
            "file-name": imfile.filename,
            "deduced-mime-type": deduced_type})
    except:
        raise internal_error_500()

user_data = {}
  
@io_router.head("/head")
async def head_endpoint():
    return Response(headers={"Custom-Header": "Ok"})

@io_router.post('/user/create')
async def create_user(username:str,
                      email:str,
                      password:str):
    try:
        user_data[username] = {
            "username" : username,
            "email" : email,
            "password": password
        }
        return ok_200(user_data[username])
    except:
        raise internal_error_500()

@io_router.put('/user/update')
async def update_user(username:str,
                      new_email:Optional[str]=None,
                      new_password:Optional[str]=None):
    try:
        old_user_data = user_data[username]
        if new_email is None:
            new_email = old_user_data["email"]
        if new_password is None:
            new_password = old_user_data["password"]
        new_user_data= {
            "username" : username,
            "email" : new_email,
            "password": new_password
        }
        user_data[username] = new_user_data
        return ok_200(user_data[username])
    except:
        raise internal_error_500()
