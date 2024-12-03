from typing import List
from fastapi import APIRouter, Depends

from app.entities.users.classes import User

from app.database.connect import AsyncSession, get_session

from app.operations.users.crud import get_all_users as get_all
from app.operations.users.crud import get_user_by_id as get_by_id


router = APIRouter(prefix="/user", tags=["User"])


@router.get("/all", response_model=List[User])
async def get_all_users(
    session: AsyncSession = Depends(get_session),
) -> List[User]:
    return await get_all(session)


@router.get("/{id}", response_model=User)
async def get_user_by_id(id: int, session: AsyncSession = Depends(get_session)) -> User:
    return await get_by_id(id, session=session)
