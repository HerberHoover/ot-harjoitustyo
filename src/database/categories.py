#categories.py
from .database import execute_query
from .database import fetch_query

def add_category(user_id, category_name):
    """
    Adds a new category for the user.

    Args:
        user_id: The unique ID of the user.
        category_name: The name of the category.
    """

    query = """
    INSERT INTO categories (user_id, name)
    VALUES (?, ?)
    """
    params = (user_id, category_name)
    execute_query(query, params)

def get_categories(user_id):
    """
    Returns all categories for the user.

    Args:
        user_id: The unique ID of the user.

    Returns:
        A list of all categories for the user.
    """
    query = """
    SELECT id, name
    FROM categories
    WHERE user_id = ?
    """
    params = (user_id,)
    return fetch_query(query, params)
