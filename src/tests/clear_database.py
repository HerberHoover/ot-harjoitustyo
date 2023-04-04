# clear_database.py

from database.database import execute_query

def clear_users_table():

    query = 'DELETE FROM users'
    execute_query(query)

if __name__ == '__main__':

    conn = create_connection()

    clear_users_table()

    conn.close()
