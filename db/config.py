from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv

load_dotenv()


DB_ENDPOINT = getenv("DB_ENDPOINT")
DB_USER = getenv("DB_USER")
DB_PASS = getenv("DB_PASS")
DB_NAME = getenv("DB_NAME")

engine_str = (
    "postgresql://" + DB_USER + ":" + DB_PASS + "@" + DB_ENDPOINT + "/" + DB_NAME
)

Engine = create_engine(engine_str)
