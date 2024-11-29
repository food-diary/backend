from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import SQL_DB

engine = create_async_engine(SQL_DB)

AsyncSessionLocal = async_sessionmaker(autoflush=False, expire_on_commit=False, bind=engine, class_=AsyncSession)

base = declarative_base()

async def get_session():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except:
            await session.close()