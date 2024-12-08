from fastapi import Depends, Response, APIRouter

from app.entities.users.classes import User, UserCreate, UserLogin

from app.database.connect import AsyncSession, get_session

from app.operations.users.auth import auth_user 
from app.operations.users.auth import register_user
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
                    session: AsyncSession = Depends(get_session)) -> dict:
    return await auth_user(user=user,
                      response=response,
                      session=session)
    
    
@router.post('/register')
async def user_reg(user: UserCreate,
                   session: AsyncSession = Depends(get_session)) -> User:
    
    return await register_user(user=user,
                          session=session)


    
    


    


  