from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response

from sqlalchemy import select

from app.database.classes import Product, ProductCreate
from app.database.models import Product as ProductDB
from app.database.database import AsyncSession, get_db
from app.database.operations.jwt.token_manager import check_verify_token


router = APIRouter(
    prefix='/product',
    tags=["Product"]
)


@router.get("", response_model=List[Product])
async def get_products(db : AsyncSession = Depends(get_db)) -> List[Product]:
    products = await db.execute(select(ProductDB))
    result = products.scalars().all()
    if not result:
        raise HTTPException(status_code=404, detail="No products found")
    return result


@router.get("/{id}", response_model=Product)
async def get_specific_product(id: int, db: AsyncSession = Depends(get_db)) -> Product:
    product = await db.execute(select(ProductDB).where(ProductDB.id == id))
    result = product.scalar()
    if not result:
        raise HTTPException(status_code=404, detail=f"Product with ID {id} not found")
    return result
    
        
@router.post("/add",response_model=Product)
async def add_product(product: ProductCreate ,db: AsyncSession = Depends(get_db),user_id: int = Depends(check_verify_token)) -> Product:
    if user_id is None:
        raise HTTPException(status_code=401,
                            detail="Пользователь не авторизирован")
        
    new_product = ProductDB(name=product.name,
                             description=product.description,
                             proteins=product.proteins,
                             fats=product.fats,
                             carbohydrates=product.carbohydrates,
                             calories=product.calories)
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    
    return new_product


@router.put('/update/{id}', response_model=Product)
async def update_specific_product(id: int,
                                  product: ProductCreate,
                                  db: AsyncSession = Depends(get_db)) -> Product:
    
    query = await db.execute(select(ProductDB).where(ProductDB.id == id))
    result = query.scalars().first()
    
    if not result:
        raise HTTPException(status_code=404, detail=f"Product with ID {id} not found.")
    
    for name, values in product.model_dump(exclude_unset=True).items():
        setattr(result, name, values)
        
    await db.commit()
    await db.refresh(result)
    
    return result



    
    