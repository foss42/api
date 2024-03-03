from fastapi import APIRouter, Depends
import foss42.text.humanize as hz
from models.text.humanize import *
from models.responses import *

humanize_router = APIRouter(tags=["Humanize"])


@humanize_router.get("/bytes")
async def humanize_bytes(data: HumanizeBytesModel = Depends()):
    try:
        res = hz.humanize_bytes(data.num,
                                data.digits,
                                data.prefix,
                                data.add_space,
                                data.trailing_zeros)
        return ok_200(res)
    except:
        raise internal_error_500()


@humanize_router.get("/social")
async def humanize_social(data: HumanizeSocialModel = Depends()):
    try:
        res = hz.humanize_social(data.num,
                                 data.digits,
                                 data.system,
                                 data.add_space,
                                 data.trailing_zeros)
        return ok_200(res)
    except:
        raise internal_error_500()


@humanize_router.get("/rank")
async def humanize_rank(data: HumanizeRankModel = Depends()):
    try:
        res = hz.humanize_rank(data.num)
        return ok_200(res)
    except:
        raise internal_error_500()


@humanize_router.get("/time")
async def humanize_time(data: HumanizeTimeModel = Depends()):
    try:
        res = hz.humanize_time(data.dt,
                               data.dt_ref,
                               data.fmt,
                               data.units,
                               data.cutoff_now,
                               data.add_adverb,
                               data.use_article,
                               data.round_down)
        return ok_200(res)
    except:
        raise internal_error_500()
