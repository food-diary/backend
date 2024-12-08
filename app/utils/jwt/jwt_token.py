from datetime import datetime, timedelta, timezone

from fastapi import HTTPException, Request

import jwt

from config import EXPIRE, ALGORITHM, SECRET_KEY



def create_access_token(data: dict, expire: int = EXPIRE):
    to_encode = data.copy()
    expire_time = datetime.now(timezone.utc) + timedelta(minutes=expire)
    to_encode.update({"exp": expire_time})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def check_verify_token(request: Request) -> int:
    get_token = request.cookies.get("access_token")

    if not get_token:
        raise HTTPException(status_code=401, detail="The token was not found. Please log in.")

    if get_token.startswith("Bearer "):
        token = get_token.split(" ")[1]
    else:
        token = get_token

    try:
        # Декодируем токен
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Ivalid token")
        return user_id
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="The token has expired. Please log in again.")
    
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Ivalid token")


    
    

    