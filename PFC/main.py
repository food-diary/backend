from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.database.operations.products.router import router as product_router
from app.database.operations.auth.router import router as auth_router
from app.database.operations.diary.router import router as diary_router

from app.database.database import engine, Base


app = FastAPI()
app.include_router(product_router)
app.include_router(auth_router)
app.include_router(diary_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем запросы с любых доменов
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем любые HTTP-методы
    allow_headers=["*"],  # Разрешаем любые заголовки
)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

#пока не нужно так как нет страницы
""" app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.get('/', response_class=HTMLResponse)
async def main_page():
    try:
        with open("frontend/page/main_page.html", 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Page not found") """
        
        
 



    
    
