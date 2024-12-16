from app.database.connect import Base

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String, index=True) 
    description = Column(String, nullable=True) 
    proteins = Column(Float) 
    fats = Column(Float) 
    carbohydrates = Column(Float) 
    calories = Column(Float) 
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    
    product_user = relationship("User", back_populates="user_product")
    product_diary = relationship("Diary", back_populates="diary_product")

