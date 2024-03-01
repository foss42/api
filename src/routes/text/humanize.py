from fastapi import APIRouter, Depends
import foss42.text.humanize as hz
from models.settings import const
from models.text.humanize import *
from routes.commons import *

humanize_router = APIRouter(tags = ["Humanize"])

@humanize_router.get("/bytes")
async def humanize_bytes(data: HumanizeBytesModel = Depends()) -> dict:
    try:
        res = hz.humanize_bytes(data.num,
                                data.digits,
                                data.prefix,
                                data.add_space,
                                data.trailing_zeros)
        return {const.k_data: res}
    except:
        raise EX_INVALID

@humanize_router.get("/social")
async def humanize_social(data: HumanizeSocialModel = Depends()) -> dict:
    try:
        res = hz.humanize_social(data.num,
                                data.digits,
                                data.system,
                                data.add_space,
                                data.trailing_zeros)
        return {const.k_data: res}
    except:
        raise EX_INVALID

@humanize_router.get("/rank")
async def humanize_rank(data: HumanizeRankModel = Depends()) -> dict:
    try:
        res = hz.humanize_rank(data.num)
        return {const.k_data: res}
    except:
        raise EX_INVALID


@humanize_router.get("/time")
async def humanize_time(data: HumanizeTimeModel = Depends()) -> dict:
    try:
        res = hz.humanize_time(data.dt,
                               data.dt_ref,
                               data.fmt,
                               data.units,
                               data.cutoff_now,
                               data.add_adverb,
                               data.use_article,
                               data.round_down)
        return {const.k_data: res}
    except:
        raise EX_INVALID
