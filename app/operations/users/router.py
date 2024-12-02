from typing import List
from fastapi import APIRouter, Depends

from app.entities.users.classes import User

from app.database.connect import AsyncSession, get_session

from app.operations.users.crud import get_all_users as get_all


router = APIRouter(prefix="/user", tags=["User"])

@router.get("/all", response_model=List[User])
async def get_all_users(
    session: AsyncSession = Depends(get_session),
) -> List[User]:
    return await get_all(session)