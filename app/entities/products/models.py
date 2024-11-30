from app.database.connect import base

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Product(base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String, index=True) 
    description = Column(String, nullable=True) 
    proteins = Column(Float) 
    fats = Column(Float) 
    carbohydrates = Column(Float) 
    calories = Column(Float) 
    user_id = Column(Integer,nullable=True, index=True)
