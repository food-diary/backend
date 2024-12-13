from datetime import date
from fastapi import HTTPException
from typing import List
from sqlalchemy import select

from sqlalchemy.orm import joinedload

from app.entities.diary.classes import Diary, DiaryCreate
from app.entities.diary.models import Diary as DiaryDB

from app.entities.products.models import Product as ProductDB

from app.database.connect import AsyncSession



async def get_records_for_day(user_id: int,
                              day: date,
                              session: AsyncSession) -> List[Diary]:
    query = await session.execute(select(DiaryDB).where(DiaryDB.user_id == user_id,
                                                            DiaryDB.day == day).options(joinedload(DiaryDB.diary_product)))
    result = query.scalars().all()
    if not result:
        raise HTTPException(status_code=404,
                            detail="Ничего не найдено!")  
              
    return [
    Diary.model_validate({
        "id": record.id,
        "product": record.diary_product,  # Должен быть объектом класса Product
        "count": record.count,
        "day": record.day
    })
    for record in result
]


async def add_new_record(data: DiaryCreate,
                        user_id: int,
                        session: AsyncSession):
    
    query = await session.execute(select(ProductDB).where(ProductDB.id == data.product_id))
    result = query.scalar_one_or_none()
    if result is None:
        raise HTTPException(status_code=404,
                            detail="Product not found!")

    new_record = DiaryDB(
                user_id=user_id,
                product_id=data.product_id,
                count=data.count,
                day=data.day
    )
    
    session.add(new_record)
    await session.commit()
    await session.refresh(new_record)
    
    return {"status" : 200,
        "msg": "Продукт успешно добавлен!"}
    
    

    