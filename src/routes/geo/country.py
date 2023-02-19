from fastapi import APIRouter, Depends
import foss42.geo.country as co
from models.settings import const
from models.geo.country import CountryCodeModel
from routes.commons import *

country_router = APIRouter(tags = ["Country Data"])

@country_router.get("/codes")
async def get_country_code_dictionary() -> dict:
    try:
        res = co.country_code_map()
        return {const.k_data: res}
    except:
        raise EX_INVALID

@country_router.get("/data")
async def get_country_data(data: CountryCodeModel = Depends()) -> dict:
    try:
        res = co.code_to_data(data.code)
        return {const.k_data: res}
    except Exception as e:
        raise custom_exception(str(e))

@country_router.get("/flag")
async def get_country_flag(data: CountryCodeModel = Depends()) -> dict:
    try:
        res = co.code_to_flag(data.code)
        return {const.k_data: res}
    except Exception as e:
        raise custom_exception(str(e))

@country_router.get("/name")
async def get_country_name(data: CountryCodeModel = Depends()) -> dict:
    try:
        res = co.code_to_popular_name(data.code)
        return {const.k_data: res}
    except Exception as e:
        raise custom_exception(str(e))

@country_router.get("/officialname")
async def get_official_country_name(data: CountryCodeModel = Depends()) -> dict:
    try:
        res = co.code_to_official_name(data.code)
        return {const.k_data: res}
    except Exception as e:
        raise custom_exception(str(e))

@country_router.get("/subdivisions")
async def get_country_subdivisions(data: CountryCodeModel = Depends()) -> dict:
    try:
        res = co.code_to_subdivision(data.code)
        return {const.k_data: res}
    except Exception as e:
        raise custom_exception(str(e))
