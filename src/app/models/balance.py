from database.expense import get_total_expense
from database.income import get_total_income

def get_balance(user_id):
    total_income = get_total_income(user_id)
    total_expense = get_total_expense(user_id)
    balance = total_income - total_expense
    return balance
