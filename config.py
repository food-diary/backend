from dotenv import load_dotenv

import os

load_dotenv()

SQL_DB = os.getenv("SQL_DB")
SQL_SYNC_DB = SQL_DB.replace("sqlite+aiosqlite", "sqlite")
