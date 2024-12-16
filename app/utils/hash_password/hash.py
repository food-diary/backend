import bcrypt


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=14)
    password = password.encode("utf-8")
    hash_password = bcrypt.hashpw(password, salt)
    return hash_password.decode("utf-8")  # Преобразуем байты в строку

def check_password(password: str, hash_pw: str) -> bool:
    password = password.encode("utf-8")
    hash_pw = hash_pw.encode("utf-8")  # Преобразуем строку обратно в байты
    return bcrypt.checkpw(password, hash_pw)
