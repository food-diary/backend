from datetime import date
from fastapi import HTTPException
from typing import List
from sqlalchemy import select

from app.entities.diary.classes import Diary, DiaryCreate
from app.entities.diary.models import Diary as DiaryDB

from app.database.connect import AsyncSession



async def get_records_for_day(user_id: int,
                              day: date,
                              session: AsyncSession) -> List[Diary]:
    query = await session.execute(select(DiaryDB).where(DiaryDB.user_id == user_id,
                                                            DiaryDB.day == day))
    result = query.scalars().all()
    if not result:
        raise HTTPException(status_code=404,
                            detail="Ничего не найдено!")        
    return result


async def add_new_record(data: DiaryCreate,
                        user_id: int,
                        session: AsyncSession) -> Diary:
    
    new_record = DiaryDB(
                user_id=user_id,
                product_id=data.product_id,
                day=data.day
    )
    
    session.add(new_record)
    await session.commit()
    await session.refresh(new_record)
    
    return new_record
    
    

    