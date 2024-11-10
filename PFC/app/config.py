from dotenv import load_dotenv
import os

load_dotenv()

SQL_DB = os.environ.get("SQL_DB")

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
TOKEN_EXPIRE_MINUTES =  int(os.environ.get("TOKEN_EXPIRE_MINUTES"))


