from pydantic import BaseModel


class TextModel(BaseModel):
    text: str

    class Config:
        json_schema_extra = {
            "example": {
                "text": "Grass is green"
            }
        }


class SlugifyModel(BaseModel):
    text: str
    sep: str = "-"

    class Config:
        json_schema_extra = {
            "example": {
                "text": "Grass is green",
                "sep":  "+"
            }
        }
