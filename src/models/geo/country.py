from pydantic import BaseModel


class CountryCodeModel(BaseModel):
    code: str

    class Config:
        json_schema_extra = {
            "example": {
                "code": "US"
            }
        }
