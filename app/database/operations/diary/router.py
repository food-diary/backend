from datetime import date
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import select

from app.database.database import AsyncSession, get_db
from app.database.classes import DayDiaryBase, Diary, DiaryCreate, DayDiary, DiaryUpdate
from app.database.models import Diary as DiaryDB, DayDiary as DayDiaryDB, Product as ProductDB
from app.database.operations.jwt.token_manager import check_verify_token

from . import crud


router = APIRouter(
    prefix='/daydiary',
    tags=['Diary']
)


@router.get('/total',response_model=List[DayDiary])
async def get_total_info(date: date = date.today,
                         db: AsyncSession = Depends(get_db),
                         user_id: int = Depends(check_verify_token)) -> List[DayDiary]:
    
    return await crud.get_total_info(db=db,
                               user_id=user_id,
                               date=date)


@router.post("/add", response_model=Diary)
async def add_product_in_diary(product: DiaryCreate,
                               db: AsyncSession = Depends(get_db),
                               user_id: int = Depends(check_verify_token)) -> Diary:
    
    return await crud.add_product_in_diary(product=product,
                                     db=db,
                                     user_id=user_id)



@router.put('/update', response_model=Diary)
async def update_diary(update_product: DiaryUpdate,
                       user_id: int = Depends(check_verify_token),
                       db: AsyncSession = Depends(get_db)) -> Diary:
    
    return await crud.update_diary(update_product=update_product,
                             user_id=user_id,
                             db=db)



