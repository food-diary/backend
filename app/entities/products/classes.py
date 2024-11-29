from pydantic import BaseModel



class ProductBase(BaseModel):
    name: str
    description: str
    proteins: float
    fats: float
    carbohydrates: float
    calories: float
    
    
class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    
    class Config:
        from_attributes = True
    