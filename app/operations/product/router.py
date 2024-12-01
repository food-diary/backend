from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy import select

from app.database.connect import get_session, AsyncSession

from app.entities.products.classes import Product
from app.entities.products.models import Product as ProductDB

from app.operations.product.crud import get_all_product as get


router = APIRouter(prefix="/product",
                   tags=["Product"])


@router.get('/all', response_model=List[Product])
async def get_all_product(session: AsyncSession = Depends(get_session)) -> List[Product]:
    return await get(session)
