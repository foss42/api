from fastapi import APIRouter, UploadFile
from routes.commons import *
from fastapi.responses import Response
import io
import mimetypes

multi_part_router = APIRouter(tags=["Multi Part"])


@multi_part_router.post('/echo_file')
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
        raise custom_exception(str(e))
