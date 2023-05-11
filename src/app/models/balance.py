from database.expense import get_total_expense, get_expense_for_category
from database.income import get_total_income, get_income_for_category

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

def get_category_balance(user_id, category_id):
    """Calculate the balance of a category by subtracting the total expenses
        from the total income for that category.

    Args:
        user_id: The unique ID of the user.
        category_id: The unique ID of the category.

    Returns:
        The calculated balance for the specified category.
    """
    total_income = get_income_for_category(user_id, category_id)
    total_expense = get_expense_for_category(user_id, category_id)
    balance = total_income - total_expense
    return balance
