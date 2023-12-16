#models_filaments.py
#from pydantic import BaseModel
#from typing import List
from config.database import Base
from sqlalchemy import Column, Integer, String, Float
"""
class Filament(BaseModel):
    id: int = 1
    name: str = "pla"
    color: str = "stelar"
    mass: float = 1000

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
      filaments: List[Filament]"""
class Filament(Base):  
    __tablename__ = "filaments"
    
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable=False) 
    color = Column(String, nullable=False)
    mass = Column(Float, nullable=False)
    
