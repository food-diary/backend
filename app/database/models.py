from sqlalchemy.sql import func
from sqlalchemy import Column, Date, DateTime, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.database.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    hashed_password = Column(String,nullable=False)
    email = Column(String, index=True, unique=True)
    created_at = Column(Date, default=func.current_date())
    
    diary_entries = relationship("Diary", back_populates="user")
    daydiary_user = relationship("DayDiary", back_populates="user_day")
    
    
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
    
    
class Diary(Base):
    __tablename__ = "user_diary"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    amount = Column(Float, nullable=False)
    created_at = Column(Date, default=func.current_date())
    
    product = relationship("Product", back_populates="diary_entries")
    user = relationship("User", back_populates="diary_entries")
    

class DayDiary(Base):
    __tablename__ = "day_diary"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id") ,nullable=False,index=True, )
    day_proteins = Column(Float) 
    day_fats  = Column(Float)
    day_carbohydrates  = Column(Float)
    day_calories = Column(Float)
    datetime = Column(Date, index=True)
    
    user_day = relationship("User", back_populates="daydiary_user")
    
    
    
    
