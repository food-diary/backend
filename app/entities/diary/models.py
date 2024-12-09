from app.database.connect import Base

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship


class Diary(Base):
    __tablename__ = "users_diary"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, )
    product_id = Column(Integer, ForeignKey("products.id"))
    count = Column(Float)
    day = Column(Date)
    
    diary_user = relationship("User", back_populates="user_diary")
    diary_product = relationship("Product", back_populates="product_diary")