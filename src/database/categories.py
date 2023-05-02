#categories.py
from .database import execute_query
from .database import fetch_query

def add_category(user_id, category_name):
    query = """
    INSERT INTO categories (user_id, name)
    VALUES (?, ?)
    """
    params = (user_id, category_name)
    execute_query(query, params)

def get_categories(user_id):
    query = """
    SELECT id, name
    FROM categories
    WHERE user_id = ?
    """
    params = (user_id,)
    return fetch_query(query, params)
