import psycopg2
from connect_db import connect_db
def create_junior_account_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS junioraccount (account_number TEXT PRIMARY KEY ,birth_certificate_number TEXT , guardian_id TEXT, name TEXT, age INTEGER , amount INTEGER , next_of_keen TEXT , account_type TEXT)""")
    conn.commit()
    conn.close()
def create_junior_account(account_number, birth_certificate_number , guardian_id , name , age , amount, next_of_keen , account_type):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO junioraccount (account_number , birth_certificate_number , guardian_id , name , age , amount , next_of_keen , account_type) VALUES (%s, %s , %s , %s,%s , %s , %s , %s)" ,  (account_number , birth_certificate_number , guardian_id , name , age , amount , next_of_keen , account_type))
        conn.commit()
        return True
    except psycopg2.IntegrityError:
        return False
    finally:
        conn.close()
def list_junior_accounts():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT account_number , birth_certificate_number , guardian_id , name , age , amount , next_of_keen FROM junioraccount")
    rows = cursor.fetchall()
    conn.close()
    return rows
def update_juinior_account_data(guardian_id , name , age , amount , next_of_keen ,account_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE junioraccount SET guardian_id = %s , name = %s , age = %s , amount = %s , next_of_keen = %s WHERE account_number = %s", (guardian_id , name , age , amount , next_of_keen , account_number))
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated > 0
def delete_junior_account(account_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM junioraccount WHERE account_number = %s" , (account_number,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted > 0
def get_one_junior_account(account_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT account_number , birth_certificate_number , guardian_id , name , age , amount , next_of_keen FROM junioraccount WHERE account_number = %s", (account_number,))
    rows = cursor.fetchone()
    conn.close()
    return rows
def search_junior__account_by_biirth_certificate_number(birth_certificate_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT account_number , birth_certificate_number , guardian_id , name , age , amount , next_of_keen FROM junioraccount WHERE birth_certificate_number = %s" , (birth_certificate_number,))
    rows = cursor.fetchone()
    conn.close()
    return rows


