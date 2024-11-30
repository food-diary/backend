from app.database.connect import base

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Users(base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, index=True, unique=True)
    hash_password = Column(String)
    
    product = relationship("Products", back_populates="user")
    