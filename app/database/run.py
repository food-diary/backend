from app.database.connect import base, engine


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)
        