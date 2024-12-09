from fastapi import FastAPI

import asyncio

import uvicorn

from app.database.run import create_database

from app.operations.product.router import router as product_router
from app.operations.users.router import router as user_router
from app.operations.users.auth_router import router as auth_router
from app.operations.diary.router import router as big_diary_router


app = FastAPI(title="Diary")
app.include_router(product_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(big_diary_router)


@app.get("/")
async def hello() -> str:
    return "Hello"


if __name__ == "__main__":
    try:
        asyncio.run(create_database())

        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
        
    except KeyboardInterrupt:
        print("Завершение работы")
