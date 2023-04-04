# src/database/create_database.py
import os
from .database import create_connection, execute_query, fetch_query

def create_tables():
    conn = create_connection()
    create_users_table = '''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                username TEXT UNIQUE,
                                password_hash TEXT
                            );'''

    show_tables_query = '''SELECT name FROM sqlite_master WHERE type='table';'''

    conn = create_connection()
    if conn is not None:
        execute_query(create_users_table)
        tables = fetch_query(show_tables_query)
        print("Tables:", tables)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")



if __name__ == '__main__':
    create_tables()
