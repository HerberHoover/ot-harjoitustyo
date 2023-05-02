# balance_controller.py
from database.income import get_total_income
from database.expense import get_total_expense
from app.models.balance import get_balance

class BalanceController:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_totals(self):
        total_income = get_total_income(self.user_id)
        total_expense = get_total_expense(self.user_id)
        balance = get_balance(self.user_id)

        return total_income, total_expense, balance
