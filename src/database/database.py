# database.py
import sqlite3
from sqlite3 import Error

DATABASE_FILE = 'budget.db'

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
    except Error as error:
        print(error)

    return conn

def close_connection(conn):
    conn.close()

def execute_query(query, params=()):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
    except Error as error:
        print(error)

    finally:
        close_connection(conn)

def fetch_query(query, params=()):
    conn = create_connection()
    cursor = conn.cursor()
    rows = None
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
    except Error as error:
        print(error)
    finally:
        close_connection(conn)
    return rows
