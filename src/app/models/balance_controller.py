# balance_controller.py
from database.income import get_total_income
from database.expense import get_total_expense
from app.models.balance import get_balance

class BalanceController:
    """
    A class to handle balance-related operations for a specific user.

    Attributes:
        user_id (int): The user ID for which the balance is managed.
    """

    def __init__(self, user_id):
        """
        Initializes a new BalanceController instance.

        Args:
            user_id (int): The user ID for which the balance is managed.
        """
        self.user_id = user_id

    def get_totals(self):
        """
        Retrieves the total income, total expense, and balance for the user.

        Returns:
            tuple: A tuple containing total income, total expense, and balance values.
        """

        total_income = get_total_income(self.user_id)
        total_expense = get_total_expense(self.user_id)
        balance = get_balance(self.user_id)

        return total_income, total_expense, balance
