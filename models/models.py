#models.py
from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True, index = True)
    first_name = Column(String, nullable=False) 
    last_name = Column(String, nullable=False)
    email = Column(Integer, nullable=False)
    gender = Column(Float, nullable=False)
    ip_address = Column(String, nullable=False)
    
