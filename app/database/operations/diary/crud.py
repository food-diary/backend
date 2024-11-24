from datetime import date
from typing import List

from fastapi import  Depends, HTTPException

from sqlalchemy import select

from app.database.database import AsyncSession, get_db
from app.database.classes import Diary, DiaryCreate, DayDiary, DiaryUpdate
from app.database.models import Diary as DiaryDB, DayDiary as DayDiaryDB, Product as ProductDB

from app.database.operations.jwt.token_manager import check_verify_token


#получение всех продуктов за день



#добавление продукта в общший дневник



#обновить продукт за день
# Обновление продукта за день



# Функция для автоматического обновления дневных данных
# Функция для автоматического обновления дневных данных


