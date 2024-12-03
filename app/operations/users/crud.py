from sqlite3 import IntegrityError
from typing import List
from sqlalchemy.exc import IntegrityError

from fastapi import HTTPException, Response
from sqlalchemy import select

from app.database.connect import AsyncSession

from app.entities.users.classes import UserCreate
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


async def delete_user_by_id(id: int, session: AsyncSession) -> Response:
    query = await session.execute(select(UserDB).where(UserDB.id == id))
    result = query.scalar_one_or_none()

    if result is None:
        raise HTTPException(status_code=401, detail="Not found!")

    await session.delete(result)
    await session.commit()

    return Response(
        status_code=204, headers={"message": "The user has been deleted!"}
    )


async def update_user_by_id(id: int,
                               user: UserCreate,
                               session: AsyncSession) -> User:
    query = await session.execute(select(UserDB).where(UserDB.id == id))
    result = query.scalar_one_or_none()
    
    if result is None:
        raise HTTPException(status_code=401, detail="Not found!")
    
    result.username=user.username
    result.hash_password=user.password
    result.email=user.email
    
    try:
        await session.commit()
        await session.refresh(result)
        
        return result
    
    except IntegrityError:
        session.rollback()    
        raise HTTPException(status_code=400, detail="Invalid request")


async def add_user(user: UserCreate,
                      session: AsyncSession) -> User:
    
    new_user = UserDB(
        username=user.username,
        hash_password=user.password,
        email=user.email,
    )
    
    try:
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        
        return new_user
    
    except IntegrityError:
        session.rollback()    
        raise HTTPException(status_code=400, detail="Invalid request")
        

