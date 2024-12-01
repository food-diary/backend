from typing import List

from fastapi import HTTPException
from sqlalchemy import select

from app.database.connect import AsyncSession

from app.entities.products.classes import Product
from app.entities.products.models import Product as ProductDB


async def get_all_product(session: AsyncSession) -> List[Product]:
    query = await session.execute(select(ProductDB))
    result = query.scalars().all()

    if not result:
        raise HTTPException(status_code=401, detail="Not found!")

    return result


async def get_product_by_id(id: int, session: AsyncSession) -> Product:
    query = await session.execute(select(ProductDB).where(ProductDB.id == id))
    result = query.scalar_one_or_none()
    
    if result is None:
        raise HTTPException(status_code=401, detail="Not found!")

    return result
