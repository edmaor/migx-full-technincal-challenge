from os import getenv
from dotenv import load_dotenv

load_dotenv()

DB_URI = getenv("DB_URI")
DB_NAME = getenv("DB_NAME")