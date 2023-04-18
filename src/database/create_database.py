# src/database/create_database.py
import os
from .database import create_connection, execute_query, fetch_query

def read_sql_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def create_tables():
    conn = create_connection()

    schema_file_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    schema_sql = read_sql_file(schema_file_path)

    sql_statements = schema_sql.split(';')

    show_tables_query = '''SELECT name FROM sqlite_master WHERE type='table';'''

    if conn is not None:
        for statement in sql_statements:
            if statement.strip():
                execute_query(statement)

        tables = fetch_query(show_tables_query)
        print("Tables:", tables)
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    create_tables()
