from pydantic import BaseModel, Field
from typing import List



class Filament(BaseModel):
    name: str = "pla"
    color: str = "stelar"
    mass: float = 1000

    class config:
        schema_extra = {
            "example": {
                "name": "pla",
                "color": "stelar",
                "mass": 1000,
            }
        }

class UpdateFilament(BaseModel):
    id: int
    name: str
    color: str 
    mass: float

    class config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "pla",
                "color": "stelar",
                "mass": 1000,
            }
        }

class ListFilaments(BaseModel):
      filaments: List[Filament]