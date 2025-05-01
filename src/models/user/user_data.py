from pydantic import BaseModel


from pydantic import BaseModel, Field
from typing import List, Optional

class UserModel(BaseModel):
    id: int
    name: str
    phone: Optional[str] = None
    email: str
    country: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": "1",
                "name": "Travis Barber",
		        "phone": "1-288-119-0313",
		        "email": "travisbarber@apidash.in",
		        "country": "United States"
            }
        }

class UserListResponseModel(BaseModel):
    data: List[UserModel]

