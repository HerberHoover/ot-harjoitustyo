from .database import execute_query
from .database import fetch_query

def add_income(user_id, amount, category_id, date, description):
    insert_income_query = """
    INSERT INTO transactions (user_id, category_id, amount, date, description, type)
    VALUES (?, ?, ?, ?, ?, 'income')
    """
    params = (user_id, category_id, amount, date, description)
    execute_query(insert_income_query, params)

def get_total_income(user_id):
    query = """
    SELECT SUM(amount) FROM transactions
    WHERE user_id = ? AND type = 'income'
    """
    result = fetch_query(query, (user_id,))
    return result[0][0] if result[0][0] else 0
