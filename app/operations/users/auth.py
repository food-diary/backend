from fastapi import HTTPException
from sqlalchemy import select

from app.entities.users.classes import UserLogin
from app.entities.users.models import User as UserDB

from app.database.connect import AsyncSession

from app.utils.hash import check_password


async def auth_user(user: UserLogin, db: AsyncSession):

    query = await db.execute(select(UserDB).where(UserDB.username == user.username))
    result = query.scalar_one_or_none()

    if result is None:
        raise HTTPException(status_code=401, detail="User not found!")

    answer: bool = check_password(user.password, result.hash_password)

    if answer is False:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return "Успех!"
