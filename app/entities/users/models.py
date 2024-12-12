from app.database.connect import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, index=True, unique=True)
    hash_password = Column(String)
    
    user_product = relationship("Product", back_populates="product_user", cascade="all, delete")
    user_diary = relationship("Diary", back_populates="diary_user", cascade="all, delete")
    