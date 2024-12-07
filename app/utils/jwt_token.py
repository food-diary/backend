from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Request

from config import EXPIRE, ALGORITHM, SECRET_KEY

import jwt


def create_access_token(data: dict, expire: int = EXPIRE):
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE)
    to_encode.update({"exp" : expire})
    encodet_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    
    return encodet_jwt


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

    
    

    