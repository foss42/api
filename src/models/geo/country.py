from pydantic import BaseModel

class CountryCodeModel(BaseModel):
    code: str

    class Config:
        schema_extra = {
            "example": {
                "code": "US"
            }
        }
