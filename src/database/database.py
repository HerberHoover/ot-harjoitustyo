# database.py
import sqlite3
from sqlite3 import Error

DATABASE_FILE = 'test.db'

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        print('connected to database')
    except Error as e:
        print(e)

    return conn

def close_connection(conn):
    conn.close()

def execute_query(query, params=()):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    close_connection(conn)

def fetch_query(query, params=()):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    close_connection(conn)
    return rows

def get_test_connection():
    return sqlite3.connect(TEST_DATABASE_NAME)