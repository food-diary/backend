from datetime import datetime, date
from pydantic import BaseModel, EmailStr, Field, NonNegativeFloat

from typing import Optional


class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Название продукта(обязательно)") 
    description: Optional[str] = Field(None, max_length=100, description="Описание продукта(не обязательно)")
    proteins: NonNegativeFloat = Field(0.0, ge=0, description="Кол-во белков(больше или равно 0)")
    fats: NonNegativeFloat = Field(0.0, ge=0, description="Кол-во жиров(больше или равно 0)")
    carbohydrates: NonNegativeFloat = Field(0.0, ge=0, description="Кол-во углеводов(больше или равно 0)")
    calories: NonNegativeFloat = Field(0.0, ge=0, le=10000, description="Кол-во калорий(больше или равно 0)")

class ProductCreate(ProductBase):
    pass
   
class Product(ProductBase):
    id: int
    
    class Config:
        from_attributes = True    
        
       
        
class UserLoginBase(BaseModel):
    username: str = Field(..., max_length=20,  description="Имя пользователя (от 3 до 50 символов)")
    password: str = Field(...,  max_length=100, description="Пароль (минимум 8 символов)")
    
class UserCreate(UserLoginBase):
    email: EmailStr = Field(..., description="Email пользователя (обязательно и в формате email)")
    created_at: date = Field(default_factory=date.today, description="Дата создания пользователя (автоматически заполняется)")

class User(BaseModel):
    id: int = Field(..., description="Уникальный идентификатор пользователя, назначаемый базой данных")
    username: str = Field(...,min_length=3, max_length=50, description="Имя пользователя (от 3 до 50 символов)")
    email: EmailStr = Field(..., description="Email пользователя")
    created_at: date = Field(..., description="Дата создания пользователя")

    class Config:
        from_attributes = True
        

        
class DiaryBase(BaseModel):
    product_id: int = Field(..., description="Продукт")
    amount: float = Field(..., ge=1, le=5000, description="Количество продукта в граммах(От 1 до 5000)")
    
class Diary(DiaryBase):
    product_id: int = Field(..., description="Уникальный идентификатор, назначаемый базой данных")
    created_at: date = Field(..., description="Дата добавления продукта")   
    
    class Config:
        from_attributes = True       
       
class DiaryCreate(DiaryBase):
    pass

class DiaryUpdate(DiaryBase):
    created_at: date = Field(default_factory=date.today,description="Дата добавления продукта")  



class DayDiaryBase(BaseModel):
    user_id: int = Field(..., description="ID пользователя")
    datetime: date = Field(..., description="Дата расчётов за день")

class DayDiary(DayDiaryBase):
    day_proteins: NonNegativeFloat = Field(0.0, description="Суммарное количество белков за день (≥ 0)")
    day_fats: NonNegativeFloat = Field(0.0, description="Суммарное количество жиров за день (≥ 0)")
    day_carbohydrates: NonNegativeFloat = Field(0.0, description="Суммарное количество углеводов за день (≥ 0)")
    day_calories: NonNegativeFloat = Field(0.0, le=10000, description="Суммарное количество калорий за день (от 0 до 10000)")

    class Config:
        from_attributes = True

class DayDiaryCreate(DayDiary):
    pass

class DayDiaryUpdate(DayDiary):
    pass
       