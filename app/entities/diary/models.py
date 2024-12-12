from app.database.connect import Base

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship


class Diary(Base):
    __tablename__ = "users_diary"
    
    id = Column(Integer, primary_key=True, index=True)
<<<<<<< HEAD
    user_id = Column(Integer, ForeignKey("users.id"), index=True, )
    product_id = Column(Integer, ForeignKey("products.id"))
<<<<<<< HEAD
    count = Column(Integer)
=======
    count = Column(Float)
>>>>>>> 1389e72 (add get_for_day func and add_new_record func)
=======
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    count = Column(Integer)
>>>>>>> 696eb06 (some edit database)
    day = Column(Date)
    
    diary_user = relationship("User", back_populates="user_diary")
    diary_product = relationship("Product", back_populates="product_diary")