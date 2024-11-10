from datetime import datetime, timedelta

from fastapi import HTTPException, Request

from jose import JWTError
import jwt

from app.config import SECRET_KEY, ALGORITHM, TOKEN_EXPIRE_MINUTES


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


def check_verify_token(request: Request):
    get_token = request.cookies.get("access_token")
    
    if not get_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    token = get_token.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user_id: int = payload.get("id")  # Извлечение user_id вместо username
        if user_id is None:
            raise HTTPException(status_code=401, detail="Пользователь не авторизирован")
        return user_id
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Сеанс истек, пожалуйста, авторизуйтесь снова")
    except JWTError:
        raise HTTPException(status_code=401, detail="Ошибка проверки токена, попробуйте авторизоваться снова")

        