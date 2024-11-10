from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.database.database import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    proteins = Column(Float)
    fats = Column(Float)
    carbohydrates = Column(Float)
    calories = Column(Float)
    
    diary_entries = relationship("Diary", back_populates="product")
    

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    hashed_password = Column(String,nullable=False)
    email = Column(String, index=True, unique=True)
    created_at = Column(DateTime, default=func.now())
    
    diary_entries = relationship("Diary", back_populates="user")
    
    
class Diary(Base):
    __tablename__ = "user_diary"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=func.now())
    #часть для подсчета
    daily_proteins = Column(Float, default=0)
    daily_fats = Column(Float, default=0)
    daily_carbohydrates = Column(Float, default=0)
    daily_calories = Column(Float, default=0)
    
    product = relationship("Product", back_populates="diary_entries")
    user = relationship("User", back_populates="diary_entries")
    
