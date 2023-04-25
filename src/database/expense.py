# expense.py
from .database import execute_query
from .database import fetch_query

def add_expense(user_id, amount, category_id, date, description):
    insert_expense_query = """
    INSERT INTO transactions (user_id, category_id, amount, date, description, type)
    VALUES (?, ?, ?, ?, ?, 'expense')
    """
    params = (user_id, category_id, amount, date, description)
    execute_query(insert_expense_query, params)

def get_total_expense(user_id):
    query = """
    SELECT SUM(amount) FROM transactions
    WHERE user_id = ? AND type = 'expense'
    """
    result = fetch_query(query, (user_id,))
    return result[0][0] if result[0][0] else 0

def get_all_expense_transactions(user_id):
    query = """
    SELECT id, user_id, category_id, amount, date, description, 'expense' as type FROM transactions
    WHERE user_id = ? AND type = 'expense'
    """
    result = fetch_query(query, (user_id,))
    return result
