from datetime import date

from pydantic import BaseModel, Field, NonNegativeInt


class DiaryBase(BaseModel):
    product_id: int = Field(..., description="ID продукта из базы данных")
    day: date = Field(..., description="Дата добавления продукта")
    
class Diary(DiaryBase):
    id: NonNegativeInt = Field(..., ge=1, description="ID записи(автогенерация в БД)")
    
    class Config:
        from_attributes = True
    
class DiaryCreate(BaseModel):
    user_id: int = Field(..., ge=1,description="ID пользователя,который добавляет продукт")
