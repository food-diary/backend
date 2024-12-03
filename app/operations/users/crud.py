from typing import List
from fastapi import HTTPException
from sqlalchemy import select

from app.database.connect import AsyncSession

from app.entities.users.models import User as UserDB
from app.entities.users.models import User


async def get_all_users(session: AsyncSession) -> List[User]:
    query = await session.execute(select(UserDB))
    result = query.scalars().all()

    if not result:
        raise HTTPException(status_code=401, detail="Not found!")

    return result


async def get_user_by_id(id: int, session: AsyncSession) -> User:
    query = await session.execute(select(UserDB).where(UserDB.id == id))
    result = query.scalar_one_or_none()

    if result is None:
        raise HTTPException(status_code=401, detail="Not found!")
    return result
