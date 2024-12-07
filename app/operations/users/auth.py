from fastapi import HTTPException, Response
from sqlalchemy import select

from app.entities.users.classes import UserLogin
from app.entities.users.models import User as UserDB

from app.database.connect import AsyncSession

from app.utils.hash import check_password

from app.utils.jwt_token import create_access_token



async def auth_user(user: UserLogin,
                    response: Response,
                    db: AsyncSession):
    query = await db.execute(select(UserDB).where(UserDB.username == user.username))
    result = query.scalar_one_or_none()

    if result is None:
        raise HTTPException(status_code=401, detail="User not found!")

    answer: bool = check_password(user.password, result.hash_password)

    if answer is False:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    user_id: int = result.id
    
    token = create_access_token({"sub" : result.username,
                        "username" : result.username,
                         "email" : result.email,
                         "id" : user_id})
    
    response.set_cookie(key="access_token", value=token, httponly=True)

    return {"status" : 200,
           "access_token": token,
            "token_type": "bearer"
    }
