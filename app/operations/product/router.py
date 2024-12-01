from typing import List

from fastapi import Depends, HTTPException, APIRouter, Response
from sqlalchemy import select

from app.database.connect import get_session, AsyncSession

from app.entities.products.classes import Product, ProductCreate

from app.operations.product.crud import get_all_product as get_all
from app.operations.product.crud import get_product_by_id as get_by_id
from app.operations.product.crud import delete_product_by_id as delete_by_id
from app.operations.product.crud import update_product_by_id as update_by_id


router = APIRouter(prefix="/product", tags=["Product"])


@router.get("/all", response_model=List[Product])
async def get_all_product(
    session: AsyncSession = Depends(get_session),
) -> List[Product]:
    return await get_all(session)



@router.get("/{id}", response_model=Product)
async def get_product_by_id(
    id: int, session: AsyncSession = Depends(get_session)
) -> Product:
    return await get_by_id(id, session=session)



@router.delete("/delete/{id}", response_class=Response)
async def delete_product_by_id(
    id: int, session: AsyncSession = Depends(get_session)
) -> Response:
    return await delete_by_id(id, session=session)



@router.patch("/update/{id}", response_model=Product)
async def update_product_by_id(
    id: int, product: ProductCreate, session: AsyncSession = Depends(get_session)
) -> Product:

    return await update_by_id(id, product=product, session=session)
