from dotenv import load_dotenv

import os

load_dotenv()

# SQL_DB = os.getenv("SQL_DB")
# SQL_SYNC_DB = SQL_DB.replace("sqlite+aiosqlite", "sqlite")

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
EXPIRE = int(os.getenv('EXPIRE'))

DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


SQL_DB = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQL_SYNC_DB = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
