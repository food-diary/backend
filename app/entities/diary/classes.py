from datetime import date

from pydantic import BaseModel, Field, NonNegativeFloat, NonNegativeInt


class DiaryBase(BaseModel):
    product_id: int = Field(..., description="ID продукта из базы данных")
<<<<<<< HEAD
<<<<<<< HEAD
    count: int = Field(0,ge=1, description="Кол-во продукта в граммах")
=======
    count: NonNegativeFloat = Field(..., description="Кол-во продукта в граммах")
>>>>>>> 1389e72 (add get_for_day func and add_new_record func)
=======
    count: NonNegativeInt = Field(..., description="Кол-во продукта в граммах")
>>>>>>> 696eb06 (some edit database)
    day: date = Field(default_factory=date.today, description="Дата добавления продукта")
    
class Diary(DiaryBase):
    id: NonNegativeInt = Field(..., ge=1, description="ID записи(автогенерация в БД)")
    
    class Config:
        from_attributes = True
    
class DiaryCreate(DiaryBase):
    pass
