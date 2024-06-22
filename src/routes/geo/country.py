from fastapi import APIRouter, Depends
import foss42.geo.country as co
from models.geo.country import CountryCodeModel
from models.responses import *

country_router = APIRouter(tags=["Country Data"])
@country_router.get("/codes")
async def get_country_code_dictionary():
    try:
        res = co.country_code_map()
        return ok_200(res)
    except:
        raise internal_error_500()
@country_router.get("/data")
async def get_country_data(data: CountryCodeModel = Depends()):
    try:
        res = co.code_to_data(data.code)
        return ok_200(res)
    except Exception as e:
        raise internal_error_500()
@country_router.get("/flag")
async def get_country_flag(data: CountryCodeModel = Depends()):
    try:
        res = co.code_to_flag(data.code)
        return ok_200(res)
    except Exception as e:
        raise internal_error_500()
@country_router.get("/name")
async def get_country_name(data: CountryCodeModel = Depends()):
    try:
        res = co.code_to_popular_name(data.code)
        return ok_200(res)
    except Exception as e:
        raise internal_error_500()
@country_router.get("/officialname")
async def get_official_country_name(data: CountryCodeModel = Depends()):
    try:
        res = co.code_to_official_name(data.code)
        return ok_200(res)
    except Exception as e:
        raise internal_error_500()
@country_router.get("/subdivisions")
async def get_country_subdivisions(data: CountryCodeModel = Depends()):
    try:
        res = co.code_to_subdivision(data.code)
        return ok_200(res)
    except Exception as e:
        raise internal_error_500()
@country_router.get("/population_density")
async def get_country_population_density(data: CountryCodeModel = Depends()):
    try:
        res = co.code_to_population_density(data.code)
        return ok_200(res)
    except Exception as e:
        raise internal_error_500()
@country_router.get("/gender_ratio")
async def get_country_gender_ratio(data: CountryCodeModel = Depends()):
    try:
        res = co.code_to_gender_ratio(data.code)
        return ok_200(res)
    except Exception as e:
        raise internal_error_500()
