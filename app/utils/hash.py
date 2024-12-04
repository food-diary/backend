import bcrypt


def hash_password(password: str):
    salt = bcrypt.gensalt(rounds=14)
    
    password = password.encode("utf-8")
    hash_password = bcrypt.hashpw(password, salt)
    
    return(hash_password)
