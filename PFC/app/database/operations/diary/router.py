from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import select

from app.database.database import AsyncSession, get_db
from app.database.classes import Diary, DiaryCreate
from app.database.models import Diary as DiaryDB
from app.database.operations.jwt.token_manager import check_verify_token


router = APIRouter(
    prefix='/diary'
)


@router.get("")
async def get_user_product(user_id: int = Depends(check_verify_token),db: AsyncSession = Depends(get_db)) -> List[Diary]:
    query = await db.execute(select(DiaryDB).where(DiaryDB.user_id == user_id))
    result = query.scalars().all()
    if not result:
        raise HTTPException(status_code=404, detail="Ничего не найдено!")
    return result


@router.post("/add", response_model=Diary)
async def add_product_in_diary(product: DiaryCreate,db: AsyncSession = Depends(get_db),user_id: int = Depends(check_verify_token)):           
    new_product = DiaryDB(product_id=product.product_id,
                          user_id=user_id,
                          amount=product.amount)
    
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    
    return new_product
    