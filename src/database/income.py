# income.py
from .database import execute_query
from .database import fetch_query

def add_income(user_id, amount, category_id, date, description):
    """
    Adds a new income transaction for the user.
    
    Args:
        user_id: The unique ID of the user.
        amount: The amount of the income.
        category_id: The ID of the category to which the income belongs.
        date: The date of the income transaction.
        description: Additional information about the income.
    """
    insert_income_query = """
    INSERT INTO transactions (user_id, category_id, amount, date, description, type)
    VALUES (?, ?, ?, ?, ?, 'income')
    """
    params = (user_id, category_id, amount, date, description)
    execute_query(insert_income_query, params)

def get_total_income(user_id):
    """
    Returns the total amount of income for the user.

    Args:
        user_id: The unique ID of the user.

    Returns:
        The total amount of income for the user.
    """
    query = """
    SELECT SUM(amount) FROM transactions
    WHERE user_id = ? AND type = 'income'
    """
    result = fetch_query(query, (user_id,))
    return result[0][0] if result[0][0] else 0

def get_all_income_transactions(user_id):
    """
    Returns all income transactions for the user.

    Args:
        user_id: The unique ID of the user.

    Returns:
        A list of all income transactions for the user.
    """
    query = """
    SELECT id, user_id, category_id, amount, date, description, 'income' as type FROM transactions
    WHERE user_id = ? AND type = 'income'
    """
    result = fetch_query(query, (user_id,))
    return result

def get_income_for_category(user_id, category_id):
    """
    Returns the total amount of income for the user for a specific category.

    Args:
        user_id: The unique ID of the user.
        category_id: The ID of the category.

    Returns:
        The total amount of income for the user for a specific category.
    """
    query = """
    SELECT SUM(amount) FROM transactions
    WHERE user_id = ? AND type = 'income' AND category_id = ?
    """
    result = fetch_query(query, (user_id, category_id))
    return result[0][0] if result[0][0] else 0

def get_all_income_transactions_for_category(user_id, category_id):
    """
    Returns all income transactions for the user for a specific category.
    
    Args:
        user_id: The unique ID of the user.
        category_id: The ID of the category.
        
    Returns:
        A list of all income transactions for the user for a specific category.
    """
    query = """
    SELECT id, user_id, category_id, amount, date, description, 'income' as type FROM transactions
    WHERE user_id = ? AND category_id = ? AND type = 'income'
    """
    result = fetch_query(query, (user_id, category_id,))
    return result
