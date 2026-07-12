import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
def connect_db():
    return psycopg2.connect(os.getenv("DATABASE_URL") ,sslmode = "require")
conn = connect_db()
cursor = conn.cursor()
