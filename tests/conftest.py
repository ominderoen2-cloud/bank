import os 
from app import app
from repositories.fixed_account import create_fixed_account_table 
from connect_db import connect_db
import pytest
@pytest.fixture
def client():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM fixedaccount")
    cursor.execute("DELETE FROM users")
    cursor.execute("DELETE FROM junioraccount")
    cursor.execute("DELETE from premiumaccount")
    cursor.execute("DELETE FROM transactions")
    conn.commit()
    conn.close()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
