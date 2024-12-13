from app.database.connect import Base


from sqlalchemy import Column, Date, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class UserDiary(Base):
    __tablename__ = "users_diary_summary"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), index=True)
    day = Column(Date, unique=True, index=True)
    sum_proteins = Column(Float)
    sum_fats = Column(Float)
    sum_carbohydrates = Column(Float)
    sum_calories = Column(Float)
    
    user_diary_users = relationship("User", back_populates="user_summary")

    