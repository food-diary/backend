from typing import Optional

from pydantic import BaseModel, Field, NonNegativeFloat, NonNegativeInt


class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_digits=15, description="Название продукта")
    description: Optional[str] = Field(None, max_length=100)
    proteins: NonNegativeFloat = Field(0.0, ge=0,description="Кол-во белков(на 100г.)")
    fats: NonNegativeFloat = Field(0.0, ge=0,description="Кол-во жиров(на 100г.)")
    carbohydrates: NonNegativeFloat = Field(0.0, ge=0,description="Кол-во углеводов(на 100г.)")
    calories: NonNegativeFloat = Field(0.0, ge=0,description="Кол-во калорий(на 100г.)")
    user_id: Optional[int] = Field(description="ID пользователя,который добавил это,если нет - None")
    
    
class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: NonNegativeInt = Field(..., ge=1, description="ID продукта(автогенерация в БД)")
    
    class Config:
        from_attributes = True
    