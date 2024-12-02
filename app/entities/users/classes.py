from pydantic import BaseModel, Field, NonNegativeInt, EmailStr


class UserBase(BaseModel):
    username: str = Field(..., min_length=2, max_length=12, description="Имя пользователя от 2 до 12 символов")
    email: EmailStr = Field(...,min_length=6, max_length=30, description="Почта в формате @email")
    
class UserCreate(BaseModel):
    password: str = Field(..., min_length=4, max_length=15, description="Пароль от 4 до 15 символов")

class User(UserBase):
    id: NonNegativeInt = Field(..., ge=1, description="ID пользователя(автогенерация в БД)")