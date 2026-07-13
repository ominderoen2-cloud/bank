import psycopg2
from connect_db import connect_db
def create_fixed_account_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS fixedaccount (account_number TEXT PRIMARY KEY , national_id TEXT , name TEXT  , age INTEGER , amount INTEGER , next_of_kin TEXT , account_type TEXT)""")
    conn.commit()
    conn.close()
def create_fixed_account(account_number , national_id , name , age , amount , next_of_kin , account_type):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO fixedaccount (account_number , national_id , name , age , amount , next_of_kin , account_type) VALUES (%s,%s,%s,%s,%s,%s,%s)" , (account_number , national_id , name , age , amount , next_of_kin, account_type))
        conn.commit()
        return True
    except psycopg2.IntegrityError:
        return False
    finally:
        conn.close()
def list_fixed_account():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT account_number , national_id , name , age , amount, next_of_kin, account_type FROM fixedaccount")
    rows = cursor.fetchall()
    conn.close()
    return rows
def update_fixed_account_data(name , age , amount , next_of_kin , account_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE fixedaccount SET name = %s , age = %s , amount = %s  , next_of_kin = %s WHERE account_number = %s",(name , age , amount , next_of_kin , account_number))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated > 0
def delete_fixed_account(account_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM fixedaccount WHERE account_number = %s", (account_number,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted > 0
def get_one_fixed_account(account_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT account_number , national_id , name , age , amount , next_of_kin , account_type FROM fixedaccount WHERE account_number = %s" , (account_number,))
    rows = cursor.fetchone()
    conn.close()
    return rows
def search_fixedaccount_by_national_id(national_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT account_number , national_id , name , age , amount , next_of_kin , account_type FROM fixedaccount WHERE national_id = %s", (national_id,))
    rows = cursor.fetchone()
    conn.close()
    return rows

