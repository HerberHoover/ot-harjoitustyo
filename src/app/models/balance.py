from database.expense import get_total_expense
from database.income import get_total_income

def get_balance(user_id):
    """Calculate the balance of a user by subtracting their total expenses from their total income.

    Args:
        user_id: The unique ID of the user.

    Returns:
        The calculated balance for the specified user.
    """
    total_income = get_total_income(user_id)
    total_expense = get_total_expense(user_id)
    balance = total_income - total_expense
    return balance
