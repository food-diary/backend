from fastapi import HTTPException, Response
from sqlalchemy import select

from app.entities.users.classes import UserLogin
from app.entities.users.models import User as UserDB

from app.database.connect import AsyncSession

from app.utils.hash_password.hash import check_password
from app.utils.jwt.jwt_token import create_access_token



async def auth_user(user: UserLogin, response: Response, db: AsyncSession):
    check_user = await db.execute(select(UserDB).where(UserDB.username == user.username))
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
        "user_id": user_db.id,
        "access_token": token,
        "token_type": "bearer"
    }