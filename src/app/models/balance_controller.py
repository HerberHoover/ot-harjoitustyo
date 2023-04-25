# balance_controller.py
from datetime import datetime
from database.income import get_total_income, add_income, get_all_income_transactions
from database.expense import get_total_expense, add_expense, get_all_expense_transactions
from app.models.balance import get_balance

class BalanceController:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_income(self, amount, category_id=None, input_date=None, description=None):
        if input_date is None:
            input_date = datetime.now()
        else:
            input_date = datetime.fromtimestamp(input_date)
        add_income(self.user_id, amount, category_id, int(input_date.timestamp()), description)

    def add_expense(self, amount, category_id=None, input_date=None, description=None):
        if input_date is None:
            input_date = datetime.now()
        else:
            input_date = datetime.fromtimestamp(input_date)
        add_expense(self.user_id, amount, category_id, int(input_date.timestamp()), description)

    def get_totals(self):
        total_income = get_total_income(self.user_id)
        total_expense = get_total_expense(self.user_id)
        balance = get_balance(self.user_id)

        return total_income, total_expense, balance

    def get_transactions(self):
        incomes = get_all_income_transactions(self.user_id)
        expenses = get_all_expense_transactions(self.user_id)
        all_transactions = incomes + expenses

        print(all_transactions)
        sorted_all = sorted(all_transactions, key=lambda x: x[4], reverse=True)
        print(sorted_all)
        return sorted_all
