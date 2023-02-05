from pydantic import BaseModel

class TextModel(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "Grass is green"
            }
        }

class SlugifyModel(BaseModel):
    text: str
    sep: str = "-"

    class Config:
        schema_extra = {
            "example": {
                "text": "Grass is green",
                "sep":  "+"
            }
        }
