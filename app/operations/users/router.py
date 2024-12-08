from typing import List
from fastapi import APIRouter, Depends, Request, Response

from app.entities.users.classes import User, UserCreate, UserLogin

from app.database.connect import AsyncSession, get_session

from app.operations.users.crud import get_all_users as get_all
from app.operations.users.crud import get_user_by_id as get_by_id
from app.operations.users.crud import delete_user_by_id as delete_by_id
from app.operations.users.crud import update_user_by_id as update_by_id
from app.operations.users.crud import add_user as add

from app.operations.users.auth_router import auth_user as auth

from app.utils.jwt.jwt_token import check_verify_token


router = APIRouter(prefix="/user", tags=["User"])

    
@router.get("/all", response_model=List[User])
async def get_all_users(
    session: AsyncSession = Depends(get_session)) -> List[User]:
    return await get_all(session)


@router.post("/add", response_model=User)
async def add_user(user: UserCreate,
                      session: AsyncSession = Depends(get_session)) -> User:
    return await add(user=user, session=session)


@router.delete("/delete/{id}", response_class=Response)
async def delete_user_by_id(id: int,
                            session: AsyncSession = Depends(get_session)) -> Response:
    return await delete_by_id(id, session=session)


@router.patch("/update/{id}", response_model=User)
async def update_user_by_id(id: int,
                            user: UserCreate,
                            session: AsyncSession = Depends(get_session)) -> User:
    return await update_by_id(id, user=user, session=session)


@router.get("/{id}", response_model=User)
async def get_user_by_id(id: int,
                         session: AsyncSession = Depends(get_session)) -> User:
    return await get_by_id(id, session=session)





