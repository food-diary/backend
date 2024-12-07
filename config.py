from dotenv import load_dotenv

import os

load_dotenv()

SQL_DB = os.getenv("SQL_DB")
SQL_SYNC_DB = SQL_DB.replace("sqlite+aiosqlite", "sqlite")

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
EXPIRE = int(os.getenv('EXPIRE'))