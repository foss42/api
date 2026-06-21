import io
import asyncio
import time
import puremagic
from typing import Annotated, Optional
from fastapi import (
    APIRouter,
    File,
    UploadFile,
    Form,
    Request,
    HTTPException,
    Response
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
        await asyncio.sleep(wait)
        return ok_200(f"Waited for {wait} seconds")
    except HTTPException:
        raise
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
        if times > 10000:
            raise bad_request_400("times cannot be more than 10000")
        res = slugify(text,
                      sep)
        if times > 1:
            res = sep.join([res,]*times)
        return ok_200(res)
    except HTTPException:
        raise
    except:
        raise internal_error_500()


MAX_BODY_SIZE = 5 * 1024 * 1024  # 5 MB

@io_router.post("/filesize")
async def create_file(request: Request):
    try:
        content_length = request.headers.get("content-length")
        if content_length and int(content_length) > MAX_BODY_SIZE:
            raise HTTPException(status_code=413, detail="Payload Too Large")
            
        content = bytearray()
        async for chunk in request.stream():
            content.extend(chunk)
            if len(content) > MAX_BODY_SIZE:
                raise HTTPException(status_code=413, detail="Payload Too Large")
                
        size = hz.humanize_bytes(len(content),
                                 2)
        header_content_type = dict(request.headers)["content-type"]
        stream = io.BytesIO(content)
        magic_conf = puremagic.magic_stream(stream)
        deduced_type = magic_conf[0].mime_type if len(magic_conf) > 0 else None
        return ok_200({"size": size,
                       "content-type": header_content_type,
                       "deduced-mime-type": deduced_type})
    except HTTPException:
        raise
    except:
        raise internal_error_500()

@io_router.post('/img')
async def analyze_img_file(
    imfile: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    try:
        if imfile.size > MAX_BODY_SIZE:
            raise HTTPException(status_code=413, detail="Payload Too Large")
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
    except HTTPException:
        raise
    except:
        raise internal_error_500()

MAX_USERS = 1000
user_data = {}
  
@io_router.post('/user/create')
async def create_user(username:str,
                      email:str,
                      password:str):
    try:
        if len(username) > 255 or len(email) > 255 or len(password) > 255:
            raise bad_request_400("Field lengths cannot exceed 255 characters")
        user_data[username] = {
            "username" : username,
            "email" : email,
            "password": password
        }
        if len(user_data) > MAX_USERS:
            oldest_key = next(iter(user_data))
            del user_data[oldest_key]
        return ok_200(user_data[username])
    except HTTPException:
        raise
    except:
        raise internal_error_500()

@io_router.put('/user/update')
async def update_user(username:str,
                      new_email:Optional[str]=None,
                      new_password:Optional[str]=None):
    try:
        if len(username) > 255 or (new_email and len(new_email) > 255) or (new_password and len(new_password) > 255):
            raise bad_request_400("Field lengths cannot exceed 255 characters")
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
    except HTTPException:
        raise
    except:
        raise internal_error_500()

@io_router.patch('/user/{username}')
async def patch_user(username: str,
                     new_email: Optional[str] = None,
                     new_password: Optional[str] = None):
    try:
        if len(username) > 255 or (new_email and len(new_email) > 255) or (new_password and len(new_password) > 255):
            raise bad_request_400("Field lengths cannot exceed 255 characters")
        if username not in user_data:
            raise not_found_404("User not found")
        if new_email is not None:
            user_data[username]["email"] = new_email
        if new_password is not None:
            user_data[username]["password"] = new_password
        return ok_200(user_data[username])
    except HTTPException:
        raise
    except:
        raise internal_error_500()

@io_router.delete('/user/{username}')
async def delete_user(username: str):
    try:
        if username not in user_data:
            raise not_found_404("User not found")
        del user_data[username]
        return ok_200({"message": "User deleted successfully"})
    except HTTPException:
        raise
    except:
        raise internal_error_500()

@io_router.head('/head')
async def head_request():
    return Response(status_code=200, headers={"X-Custom-Head": "HEAD works"})

@io_router.post('/octet-stream')
async def octet_stream_request(request: Request):
    try:
        content_type = request.headers.get("content-type")
        if content_type != "application/octet-stream":
            raise bad_request_400("Content-Type must be application/octet-stream")
            
        content_length = request.headers.get("content-length")
        if content_length and int(content_length) > MAX_BODY_SIZE:
            raise HTTPException(status_code=413, detail="Payload Too Large")
            
        size_bytes = 0
        async for chunk in request.stream():
            size_bytes += len(chunk)
            if size_bytes > MAX_BODY_SIZE:
                raise HTTPException(status_code=413, detail="Payload Too Large")
                
        size = hz.humanize_bytes(size_bytes, 2)
        return ok_200({"size": size, "message": "Octet stream processed successfully"})
    except HTTPException:
        raise
    except:
        raise internal_error_500()

