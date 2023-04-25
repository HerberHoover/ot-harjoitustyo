#categories.py
from .database import execute_query

def add_category(user_id, category_name):
    query = """
    INSERT INTO categories (user_id, name)
    VALUES (?, ?)
    """
    params = (user_id, category_name)
    execute_query(query, params)
    print(f"Category {category_name} added successfully.")
