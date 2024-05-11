from fastapi import APIRouter, Depends
import foss42.geo.country as co
from models.geo.country import CountryCodeModel
from models.responses import *

country_router = APIRouter(tags=["Country Data"])


@country_router.get("/codes")
async def get_country_code_dictionary():
    """
    Description:
        
        This API fetches the country code dictionary where country names are keys and the Alpha-2 (two-lettered) country codes are the values corresponding to the keys.
    
    Args:
            
        None

    Returns:
        
        The country code dictionary where country names are keys and the Alpha-2 (two-lettered) country codes are the values corresponding to the keys.

        example:
                
                {    
                    "data": {
                            "Afghanistan": "AF",
                            "Albania": "AL",
                            "Algeria": "DZ",
                            "American Samoa": "AS",
                            "Andorra": "AD",
                            "Angola": "AO",
                            ...
                        }
                }

    Raises:
        
        HTTPException: If an internal server error occurs.
    """
    try:
        res = co.country_code_map()
        return ok_200(res)
    except:
        raise internal_error_500()


@country_router.get("/data")
async def get_country_data(data: CountryCodeModel = Depends()):
    """
    Description:
    
        This API fetches some world bank data of a country given by its ISO Alpha-2 or Alpha-3 country code.

    Args:

        data (CountryCodeModel): The country code model containing the country code.

    Returns:

        dict: The country data.

        example:

            {
                "data": {
                    "area": 9831510,
                    "population": 331893745
                }   
            }

    Raises:

        HTTPException: If an error occurs while retrieving the country data.
    
    """
    try:
        res = co.code_to_data(data.code)
        return ok_200(res)
    except Exception as e:
        raise internal_error_500()


@country_router.get("/flag")
async def get_country_flag(data: CountryCodeModel = Depends()):
    """
    Description:

        This API fetches the emoji country flag corresponding to an ISO Alpha-2 or Alpha-3 country code.

    Args:
    
        data (CountryCodeModel): The country code model containing the country code.
    
    Returns:
        
            dict: The country flag.
        
            example:
            
                {
                    "data": "🇦🇫"
                }
    
    Raises:
            
        HTTPException: If an error occurs while retrieving the country flag.

    
    """
    try:
        res = co.code_to_flag(data.code)
        return ok_200(res)
    except Exception as e:
        raise internal_error_500()


@country_router.get("/name")
async def get_country_name(data: CountryCodeModel = Depends()):
    """
    Description:
        
        This API fetches the name by which a country is popularly know as, for the given Alpha-3 or Alpha-2 country code.

    Args:
            
            data (CountryCodeModel): The country code model containing the country code.
    
    Returns:
            
            dict: The popular name of the country.
            
            example:
            
                {
                    "data": "Afghanistan"
                }
    
    Raises:
                
            HTTPException: If an error occurs while retrieving the popular name of the country.



    """
    try:
        res = co.code_to_popular_name(data.code)
        return ok_200(res)
    except Exception as e:
        raise internal_error_500()


@country_router.get("/officialname")
async def get_official_country_name(data: CountryCodeModel = Depends()):
    """
    Description:

        This API fetches the official (ISO) country name for an Alpha-3 or Alpha-2 country code.
    Args:
    
        data (CountryCodeModel): The country code model containing the country code.
    
    Returns:
        
            dict: The official name of the country.
        
            example:
        
                {
                    "data": "Viet Nam"
                }
    
    Raises:
            
        HTTPException: If an error occurs while retrieving the official name of the country.
    """
    try:
        res = co.code_to_official_name(data.code)
        return ok_200(res)
    except Exception as e:
        raise internal_error_500()


@country_router.get("/subdivisions")
async def get_country_subdivisions(data: CountryCodeModel = Depends()):
    """
    Description:
        
        This API fetches the country subdivision details (states, territories, etc.) for the given two letter (Alpha-2) or three letter (Alpha-3) ISO 3166-1 country code.

    Args:
        
        data (CountryCodeModel): The country code model containing the country code.
    
    Returns:
            
            dict: The country subdivision details.
            
            example:

                {
                  "data": [
                    {
                      "code": "ACT",
                      "name": "Australian Capital Territory",
                      "category": "territory"
                    },
                    {
                      "code": "NSW",
                      "name": "New South Wales",
                      "category": "state"
                    },
                    {
                      "code": "NT",
                      "name": "Northern Territory",
                      "category": "territory"
                    },
                    {
                      "code": "QLD",
                      "name": "Queensland",
                      "category": "state"
                    },
                    {
                      "code": "SA",
                      "name": "South Australia",
                      "category": "state"
                    },
                    {
                      "code": "TAS",
                      "name": "Tasmania",
                      "category": "state"
                    },
                    {
                      "code": "VIC",
                      "name": "Victoria",
                      "category": "state"
                    },
                    {
                      "code": "WA",
                      "name": "Western Australia",
                      "category": "state"
                    }
                  ]
                }
        
    Raises:
                
        HTTPException: If an error occurs while retrieving the country subdivision details.
    """
    try:
        res = co.code_to_subdivision(data.code)
        return ok_200(res)
    except Exception as e:
        raise internal_error_500()
