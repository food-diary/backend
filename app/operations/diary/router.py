from fastapi import APIRouter, HTTPException
from typing import List
from fastapi import APIRouter, Depends, Response
from sqlalchemy import select

from app.entities.diary.classes import Diary
from app.entities.diary.models import Diary as DiaryDB

from app.database.connect import AsyncSession, get_session
from app.utils.jwt.jwt_token import check_verify_token



router = APIRouter(prefix='/diary',
                   tags=['Big diary'])


@router.get("/all", response_model=List[Diary])
async def get_records_for_day(user_id: int = Depends(check_verify_token),
                              session: AsyncSession = Depends(get_session)) -> List[Diary]:
    
    query = await session.execute(select(DiaryDB).where(DiaryDB.user_id == user_id))
    result = query.scalars().all()
    if not result:
        raise HTTPException(status_code=404,
                            detail="Ничего не найдено!")
        
    return result