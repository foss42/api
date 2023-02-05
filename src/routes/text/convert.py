from fastapi import APIRouter, Depends
import foss42.text.translate as tl
from foss42.text.slugify import slugify
from models.settings import const
from models.text.text import TextModel, SlugifyModel
from routes.commons import *

text_conversion_router = APIRouter(tags = ["Text Conversion"])

@text_conversion_router.get("/slug")
async def to_slug(data: SlugifyModel = Depends()) -> dict:
    try:
        res = slugify(data.text, 
                      data.sep)
        return {const.k_data: res}
    except:
        raise ex_invalid

@text_conversion_router.get("/phone2numeric")
async def phone_number_to_numeric(data: TextModel = Depends()) -> dict:
    try:
        res = tl.phone2numeric(data.text)
        return {const.k_data: res}
    except:
        raise ex_invalid

@text_conversion_router.get("/leet")
async def to_leet(data: TextModel = Depends()) -> dict:
    try:
        res = tl.leet(data.text)
        return {const.k_data: res}
    except:
        raise ex_invalid

@text_conversion_router.get("/upsidedown")
async def to_upside_down(data: TextModel = Depends()) -> dict:
    try:
        res = tl.upside_down(data.text)
        return {const.k_data: res}
    except:
        raise ex_invalid

@text_conversion_router.get("/mirror")
async def to_mirror(data: TextModel = Depends()) -> dict:
    try:
        res = tl.mirror(data.text)
        return {const.k_data: res}
    except:
        raise ex_invalid
