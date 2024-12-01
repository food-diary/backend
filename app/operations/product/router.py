from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy import select

from app.database.connect import get_session, AsyncSession

from app.entities.products.classes import Product
from app.entities.products.models import Product as ProductDB


router = APIRouter(prefix="/product",
                   tags=["Product"])


@router.get('/all', response_model=List[Product])
async def get_all_product(session: AsyncSession = Depends(get_session)) -> List[Product]:
    query = await session.execute(select(ProductDB))
    result = query.scalars().all()
    
    if not result:
        raise HTTPException(status_code=401,
                            detail="Not found!")
    
    return result
