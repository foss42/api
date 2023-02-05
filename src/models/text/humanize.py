from enum import Enum
from typing import Optional
from pydantic import Field, BaseModel, NonNegativeInt 
from fastapi import Query

class HumanizeBytesModel(BaseModel):
    num: NonNegativeInt
    digits: int = 0
    prefix: bool = False
    add_space: bool = True
    trailing_zeros: bool = False

    class Config:
        schema_extra = {
            "example": {
                "num": 24117248,
                "digits": 0,
                "add_space": False
            }
        }        

class SystemEnum(str, Enum):
    na = "NA"
    uk = "UK"
    ss = "SS"

class HumanizeSocialModel(BaseModel):
    num: NonNegativeInt
    digits: int = 1
    system: SystemEnum = SystemEnum.na
    add_space: bool = False
    trailing_zeros: bool = False

    class Config:
        schema_extra = {
            "example": {
                "num": 24117248,
                "digits": 0,
                "add_space": False,
                "system": "UK"
            }
        } 

class HumanizeRankModel(BaseModel):
    num: NonNegativeInt
    to_words: bool = False

    class Config:
        schema_extra = {
            "example": {
                "num": 3,
                "to_words": True
            }
        } 

class DateUnitsEnum(str, Enum):
    full = "FULL"
    short = "SHORT"

class HumanizeTimeModel(BaseModel):
    dt: str
    dt_ref: Optional[str] = None
    fmt: Optional[str] = None
    units: DateUnitsEnum = DateUnitsEnum.full
    cutoff_now: NonNegativeInt = 1
    add_adverb: bool = False
    use_article: bool = False
    round_down: bool = True        

    class Config:
        schema_extra = {
            "example": {
                "dt": '2020-12-27T18:31:29',
                "add_adverb": True, 
                "use_article": True
            }
        } 
