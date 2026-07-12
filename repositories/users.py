import psycopg2
from connect_db import connect_db
def create_users_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY , password TEXT NOT NULL)""")
    conn.commit()
    conn.close()
def add_users(username , password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username , password) VALUES (%s , %s)", (username , password))
        conn.commit()
        return True
    except psycopg2.IntegrityError:
        return False
    finally :
        conn.close()
def get_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows
def get_one_user(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password FROM users WHERE username = %s",
        (username,)
    )
    rows = cursor.fetchone()
    conn.close()
    return rows
def update_user(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET username = %s", (username,))
    updated = cursor.rowcount
    conn.close()
    return updated
def delete_user(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE username FROM users", (username,))
    deleted = cursor.rowcount()
    conn.close()
    return deleted

