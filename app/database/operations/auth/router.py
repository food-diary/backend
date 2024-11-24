from fastapi import HTTPException, Depends, APIRouter
from fastapi import Response

from sqlalchemy import select

from passlib.context import CryptContext

from app.database.classes import UserCreate, User, UserLoginBase
from app.database.database import AsyncSession, get_db
from app.database.models import User as UserDB

from app.database.operations.jwt.token_manager import create_token, check_verify_token


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
    )

# Хэширование пароля
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/register", response_model=User)
async def reg_user(user: UserCreate, db: AsyncSession = Depends(get_db)) -> User: 
    check_user = await db.execute(select(UserDB).where(UserDB.username == user.username))
    check_email = await db.execute(select(UserDB).where(UserDB.email == user.email))
    
    if check_user.scalar() is not None:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    elif check_email.scalar() is not None:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = pwd_context.hash(user.password)
    new_user = UserDB(
        username=user.username,
        hashed_password=hashed_password,
        email=user.email 
    )
            
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)       
    return new_user


@router.post("/login")
async def sing_in(user: UserLoginBase,response: Response, db: AsyncSession = Depends(get_db)):
    check_user = await db.execute(select(UserDB).where(UserDB.username == user.username))
    user_db = check_user.scalar_one_or_none()
    
    if user_db is None:
        raise HTTPException(status_code=400, detail="Username is not found!")
    
    if not pwd_context.verify(user.password, user_db.hashed_password):
        raise HTTPException(status_code=400, detail="Password is not correct!")
    
    user_id = await db.execute(select(UserDB.id).where(UserDB.username == user.username))
    id = user_id.scalar()
    
    token = create_token({
        "sub": user.username,
        "username": user.username,
        "id": id
    })
    
    response.set_cookie(key="access_token", value=f"Bearer {token}", httponly=True)
    
    return {
        "status": 200,
        "access_token": token,
        "token_type": "bearer"
    }
    
@router.get("/check")
async def check_token(user_id: int = Depends(check_verify_token)):
    return {
        "message" : f"Привет, ваш айди - {user_id}"
    }
    
