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
    
@country_router.get("/phonecodes")
async def get_country_phonecodes(data: CountryCodeModel = Depends()):
    try:
        res = co.code_to_phone_code(data.code)
        if res:
            return ok_200(res)
        else:
            return not_found_404("Phone code not found for the given country code.")
    except KeyError:
        return bad_request_400("Invalid country code provided.")
    except Exception as e:
        return internal_error_500(str(e))
