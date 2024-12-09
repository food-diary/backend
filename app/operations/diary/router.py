from datetime import date

from fastapi import APIRouter,Depends

from typing import List

from app.entities.diary.classes import Diary, DiaryCreate

from app.database.connect import AsyncSession, get_session
from app.utils.jwt.jwt_token import check_verify_token
from app.operations.diary.crud import get_records_for_day as get_for_day
from app.operations.diary.crud import add_new_record as new_record



router = APIRouter(prefix='/diary',
                   tags=['Big diary'])


@router.get("/all", response_model=List[Diary])
async def get_records_for_day(user_id: int = Depends(check_verify_token),
                              session: AsyncSession = Depends(get_session),
                              day: date = date.today()) -> List[Diary]:
    
    return await get_for_day(user_id=user_id,
                             session=session,
                             day=day)
    
    
@router.post("/add", response_model=Diary)
async def add_new_record(data: DiaryCreate,
                        user_id: int = Depends(check_verify_token),
                        session: AsyncSession = Depends(get_session)) -> Diary:
    
    return await new_record(data=data,
                            user_id=user_id,
                            session=session)