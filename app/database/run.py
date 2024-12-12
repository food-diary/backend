from app.entities.products import models
from app.entities.users import models
from app.entities.diary import models
from app.database.connect import Base, engine


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        