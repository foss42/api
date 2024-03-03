from fastapi import APIRouter, Depends
from typing import Callable
import foss42.text.convert as cc
from models.text.text import TextModel
from models.responses import *

case_convert_router = APIRouter(tags=["Case Conversion"])


def _convert(text: str, func: Callable):
    try:
        res = func(text)
        return ok_200(res)
    except:
        raise internal_error_500()


@case_convert_router.post("/lower")
async def to_lower_case(data: TextModel):
    return _convert(data.text, cc.lower_case)


@case_convert_router.get("/lower")
async def to_lower_case(data: TextModel = Depends()):
    return _convert(data.text, cc.lower_case)


@case_convert_router.post("/upper")
async def to_upper_case(data: TextModel):
    return _convert(data.text, cc.upper_case)


@case_convert_router.get("/upper")
async def to_upper_case(data: TextModel = Depends()):
    return _convert(data.text, cc.upper_case)


@case_convert_router.post("/capital")
async def to_capital_case(data: TextModel):
    return _convert(data.text, cc.capital_case)


@case_convert_router.get("/capital")
async def to_capital_case(data: TextModel = Depends()):
    return _convert(data.text, cc.capital_case)


@case_convert_router.post("/title")
async def to_title_case(data: TextModel):
    return _convert(data.text, cc.title_case)


@case_convert_router.get("/title")
async def to_title_case(data: TextModel = Depends()):
    return _convert(data.text, cc.title_case)


@case_convert_router.post("/sentence")
async def to_sentence_case(data: TextModel):
    return _convert(data.text, cc.sentence_case)


@case_convert_router.get("/sentence")
async def to_sentence_case(data: TextModel = Depends()):
    return _convert(data.text, cc.sentence_case)


@case_convert_router.get("/swap")
async def to_swap_case(data: TextModel = Depends()):
    return _convert(data.text, cc.swap_case)


@case_convert_router.get("/flat")
async def to_flat_case(data: TextModel = Depends()):
    return _convert(data.text, cc.flat_case)


@case_convert_router.get("/pascal")
async def to_pascal_case(data: TextModel = Depends()):
    return _convert(data.text, cc.pascal_case)


@case_convert_router.get("/camel")
async def to_camel_case(data: TextModel = Depends()):
    return _convert(data.text, cc.camel_case)


@case_convert_router.get("/snake")
async def to_snake_case(data: TextModel = Depends()):
    return _convert(data.text, cc.snake_case)


@case_convert_router.get("/constant")
async def to_constant_case(data: TextModel = Depends()):
    return _convert(data.text, cc.constant_case)


@case_convert_router.get("/camelsnake")
async def to_camel_snake_case(data: TextModel = Depends()):
    return _convert(data.text, cc.camel_snake_case)


@case_convert_router.get("/pascalsnake")
async def to_pascal_snake_case(data: TextModel = Depends()):
    return _convert(data.text, cc.pascal_snake_case)


@case_convert_router.get("/dot")
async def to_dot_case(data: TextModel = Depends()):
    return _convert(data.text, cc.dot_case)


@case_convert_router.get("/kebab")
async def to_kebab_case(data: TextModel = Depends()):
    return _convert(data.text, cc.kebab_case)


@case_convert_router.get("/cobol")
async def to_cobol_case(data: TextModel = Depends()):
    return _convert(data.text, cc.cobol_case)


@case_convert_router.get("/train")
async def to_train_case(data: TextModel = Depends()):
    return _convert(data.text, cc.train_case)


@case_convert_router.get("/camel2lower")
async def camel_to_lower_case(data: TextModel = Depends()):
    return _convert(data.text, cc.camel_to_lower)


@case_convert_router.get("/snake2lower")
async def snake_to_lower_case(data: TextModel = Depends()):
    return _convert(data.text, cc.snake_to_lower)


@case_convert_router.get("/kebab2lower")
async def kebab_to_lower_case(data: TextModel = Depends()):
    return _convert(data.text, cc.kebab_to_lower)
