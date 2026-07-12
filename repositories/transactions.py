import psycopg2
from connect_db import connect_db
def create_transactions_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS transactions (transaction_id  TEXT PRIMARY KEY , account_from TEXT  , account_to TEXT, amount INTEGER  , account_from_balance INTEGER,account_to_balance INTEGER , transaction_time TIMESTAMP)""")
    conn.commit()
    conn.close()
def add_transaction(transaction_id , account_from , account_to ,amount , account_from_balance , account_to_balance , transaction_time):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO transactions (transaction_id , account_from , account_to , amount , account_from_balance ,account_to_balance , transaction_time) VALUES (%s , %s , %s , %s ,%s ,%s ,%s)", (transaction_id , account_from , account_to ,amount,account_from_balance , account_to_balance, transaction_time))
        conn.commit()
        return True
    except psycopg2.IntegrityError:
        return False
    finally:
        conn.close()
def get_one_transactions(transaction_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT transaction_id,
               account_from,
               account_to,
               amount,
               account_from_balance,
               account_to_balance,
               transaction_time
        FROM transactions
        WHERE transaction_id = %s
        """,
        (transaction_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "transaction_id": row[0],
        "account_from": row[1],
        "account_to": row[2],
        "amount": row[3],
        "account_from_balance": row[4],
        "account_to_balance": row[5],
        "transaction_time": row[6].isoformat()
    }
def get_all_transactions():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT transaction_id,
               account_from,
               account_to,
               amount,
               account_from_balance,
               account_to_balance,
               transaction_time
        FROM transactions
    """)

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "transaction_id": row[0],
            "account_from": row[1],
            "account_to": row[2],
            "amount": row[3],
            "account_from_balance": row[4],
            "account_to_balance": row[5],
            "transaction_time": row[6].isoformat()
        }
        for row in rows
    ]
def update_transaction(account_from_balance,
                       account_to_balance,
                       transaction_time,
                       transaction_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE transactions
        SET account_from_balance = %s,
            account_to_balance = %s,
            transaction_time = %s
        WHERE transaction_id = %s
        """,
        (
            account_from_balance,
            account_to_balance,
            transaction_time,
            transaction_id
        )
    )

    conn.commit()
    updated = cursor.rowcount
    conn.close()

    return updated

