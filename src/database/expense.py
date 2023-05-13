# expense.py
from .database import execute_query
from .database import fetch_query

def add_expense(user_id, amount, category_id, date, description):
    """
    Adds a new expense transaction for the user.

    Args:
        user_id: The unique ID of the user.
        amount: The amount of the expense.
        category_id: The ID of the category to which the expense belongs.
        date: The date of the expense transaction.
        description: Additional information about the expense.
    """
    insert_expense_query = """
    INSERT INTO transactions (user_id, category_id, amount, date, description, type)
    VALUES (?, ?, ?, ?, ?, 'expense')
    """
    params = (user_id, category_id, amount, date, description)
    execute_query(insert_expense_query, params)

def get_total_expense(user_id):
    """
    Returns the total amount of expense for the user.

    Args:
        user_id: The unique ID of the user.

    Returns:
        The total amount of expense for the user.
    """
    query = """
    SELECT SUM(amount) FROM transactions
    WHERE user_id = ? AND type = 'expense'
    """
    result = fetch_query(query, (user_id,))
    return result[0][0] if result[0][0] else 0

def get_all_expense_transactions(user_id):
    """
    Returns all expense transactions for the user.

    Args:
        user_id: The unique ID of the user.

    Returns:
        A list of all expense transactions for the user.
    """
    query = """
    SELECT id, user_id, category_id, amount, date, description, 'expense' as type FROM transactions
    WHERE user_id = ? AND type = 'expense'
    """
    result = fetch_query(query, (user_id,))
    return result

def get_expense_for_category(user_id, category_id):
    """
    Returns the total amount of expense for the user for a specific category.

    Args:
        user_id: The unique ID of the user.
        category_id: The ID of the category.

    Returns:
        The total amount of expense for the user for a specific category.
    """
    query = """
    SELECT SUM(amount) FROM transactions
    WHERE user_id = ? AND type = 'expense' AND category_id = ?
    """
    result = fetch_query(query, (user_id, category_id))
    return result[0][0] if result[0][0] else 0

def get_all_expense_transactions_for_category(user_id, category_id):
    """
    Returns all expense transactions for the user for a specific category.

    Args:
        user_id: The unique ID of the user.
        category_id: The ID of the category.

    Returns:
        A list of all expense transactions for the user for a specific category.
    """
    query = """
    SELECT id, user_id, category_id, amount, date, description, 'expense' as type FROM transactions
    WHERE user_id = ? AND category_id = ? AND type = 'expense'
    """
    result = fetch_query(query, (user_id, category_id,))
    return result
