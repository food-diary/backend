from datetime import date

from pydantic import BaseModel, Field, NonNegativeFloat, NonNegativeInt


class DiaryBase(BaseModel):
    product_id: int = Field(..., description="ID продукта из базы данных")
    count: NonNegativeInt = Field(..., description="Кол-во продукта в граммах")
    day: date = Field(default_factory=date.today, description="Дата добавления продукта")
    
class Diary(DiaryBase):
    id: NonNegativeInt = Field(..., ge=1, description="ID записи(автогенерация в БД)")
    
    class Config:
        from_attributes = True
    
class DiaryCreate(DiaryBase):
    pass
