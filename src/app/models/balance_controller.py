from database.income import get_total_income, add_income
from database.expense import get_total_expense, add_expense
from app.models.balance import get_balance

class BalanceController:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_income(self, amount):
        add_income(self.user_id, amount, None, None, None)

    def add_expense(self, amount):
        add_expense(self.user_id, amount, None, None, None)

    def get_totals(self):
        total_income = get_total_income(self.user_id)
        total_expense = get_total_expense(self.user_id)
        balance = get_balance(self.user_id)

        return total_income, total_expense, balance
