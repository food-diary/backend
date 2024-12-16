from datetime import date

from pydantic import BaseModel, Field, NonNegativeFloat, NonNegativeInt


class UserDiaryBase(BaseModel):
    day: date = Field(default_factory=date.today, description="Дата добавления продукта")
    sum_proteins: NonNegativeFloat = Field(0.0, ge=0,description="Кол-во белков(сумма)")
    sum_fats: NonNegativeFloat = Field(0.0, ge=0,description="Кол-во жиров(сумма)")
    sum_carbohydrates: NonNegativeFloat = Field(0.0, ge=0,description="Кол-во углеводов(сумма)")
    sum_calories: NonNegativeFloat = Field(0.0, ge=0,description="Кол-во калорий(сумма)")
    
    
class UserDiary(UserDiaryBase):
    pass

class UserDiaryCreate(UserDiaryBase):
    user_id: NonNegativeInt = Field(..., description="ID пользователя,который добавил это,если нет - None")