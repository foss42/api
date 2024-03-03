from fastapi import APIRouter, Depends
import foss42.text.translate as tl
from foss42.text.slugify import slugify
from models.text.text import TextModel, SlugifyModel
from models.responses import *

text_conversion_router = APIRouter(tags=["Text Conversion"])


@text_conversion_router.get("/slug")
async def to_slug(data: SlugifyModel = Depends()):
    try:
        res = slugify(data.text,
                      data.sep)
        return ok_200(res)
    except:
        raise internal_error_500()


@text_conversion_router.get("/phone2numeric")
async def phone_number_to_numeric(data: TextModel = Depends()):
    try:
        res = tl.phone2numeric(data.text)
        return ok_200(res)
    except:
        raise internal_error_500()


@text_conversion_router.get("/leet")
async def to_leet(data: TextModel = Depends()):
    try:
        res = tl.leet(data.text)
        return ok_200(res)
    except:
        raise internal_error_500()


@text_conversion_router.get("/upsidedown")
async def to_upside_down(data: TextModel = Depends()):
    try:
        res = tl.upside_down(data.text)
        return ok_200(res)
    except:
        raise internal_error_500()


@text_conversion_router.get("/mirror")
async def to_mirror(data: TextModel = Depends()):
    try:
        res = tl.mirror(data.text)
        return ok_200(res)
    except:
        raise internal_error_500()
