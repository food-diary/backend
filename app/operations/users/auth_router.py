from fastapi import Depends, Response, APIRouter

from app.entities.users.classes import UserLogin

from app.database.connect import AsyncSession, get_session

from app.operations.users.auth import auth_user 
from app.utils.jwt.jwt_token import check_verify_token



router = APIRouter(prefix='/auth',
                   tags=["Auth"])


@router.get("/check")
async def check_token(user_id: int = Depends(check_verify_token)):
    return {
        "message": f"Привет, ваш ID - {user_id}"
    }


@router.post('/login')
async def user_auth(user: UserLogin,
                    response: Response,
                    db: AsyncSession = Depends(get_session)):
    return await auth_user(user=user,
                      response=response,
                      db=db)

    
    


    


  