from datetime import date
from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy import select
from app.utils.jwt.jwt_token import check_verify_token

from app.entities.users_diary.models import UserDiary as UserDiaryDB
from app.database.connect import AsyncSession, get_session


router = APIRouter(prefix="/users_diary_sum",
                   tags=['Diary Sum'])

@router.get('')
async def get_sum_calories(day: date = date.today(),
                        session: AsyncSession= Depends(get_session),
                           user_id: int = Depends(check_verify_token)):
    
    query = await session.execute(select(UserDiaryDB).where(UserDiaryDB.day == day,
                                                            UserDiaryDB.user_id == user_id))
    result = query.scalar_one_or_none()
    
    if result is None:
        raise HTTPException(status_code=404,
                            detail="Not found!")
        
    return result