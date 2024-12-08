from sqlite3 import IntegrityError
from typing import List
from sqlalchemy.exc import IntegrityError

from fastapi import HTTPException, Response
from sqlalchemy import select

from app.database.connect import AsyncSession

from app.entities.users.classes import UserCreate, UserLogin
from app.entities.users.models import User as UserDB
from app.entities.users.models import User


from app.utils.hash_password.hash import check_password, hash_password as hash_pw
from app.utils.jwt.jwt_token import create_access_token



async def auth_user(user: UserLogin, response: Response, session: AsyncSession) -> dict:
    check_user = await session.execute(select(UserDB).where(UserDB.username == user.username))
    user_db = check_user.scalar_one_or_none()

    if user_db is None:
        raise HTTPException(status_code=400, detail="Пользователь не найден!")

    is_password_correct = check_password(user.password, user_db.hash_password)

    if not is_password_correct:
        raise HTTPException(status_code=401, detail="Неверное имя пользователя или пароль.")

    token = create_access_token({
        "sub": user.username,
        "username": user.username,
        "id": user_db.id
    })

    response.set_cookie(key="access_token", value=f"Bearer {token}", httponly=True)

    return {
        "status": 200,
        "access_token": token,
        "token_type": "bearer"
    }
    
    
async def register_user(user: UserCreate,
                      session: AsyncSession) -> User:
    hash_password = hash_pw(user.password)
    
    new_user = UserDB(
        username=user.username,
        hash_password=hash_password,
        email=user.email,
    )
    
    try:
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        
        return new_user
    
    except IntegrityError:
        await session.rollback()    
        raise HTTPException(status_code=400,
                            detail="The username or email address is already occupied!")