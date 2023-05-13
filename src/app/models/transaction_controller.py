# transaction_controller.py
from datetime import datetime
from database.income import add_income, get_all_income_transactions
from database.expense import add_expense, get_all_expense_transactions
from database.income import get_all_income_transactions_for_category
from database.expense import get_all_expense_transactions_for_category

from .category_controller import CategoryController

class TransactionController:
    """
    A class to manage transactions including income and expenses for a specific user.

    Attributes:
        user_id: The unique ID of the user.
        category_controller: An instance of CategoryController associated with the user.
    """

    def __init__(self, user_id, category_controller: CategoryController):
        """
        Initializes a new TransactionController instance.

        Args:
            user_id: The unique ID of the user.
            category_controller: An instance of CategoryController associated with the user.
        """
        self.user_id = user_id
        self.category_controller = category_controller

    def add_income(self, amount, category_id=None, input_date=None, description=None):
        """
        Adds a new income transaction for the user.

        Args:
            amount: The amount of the income.
            category_id: The ID of the category to which the income belongs.
            input_date: The date of the income transaction.
            description: Additional information about the income.
        """
        if input_date is None:
            input_date = datetime.now()
        else:
            input_date = datetime.fromtimestamp(input_date)
        add_income(self.user_id, amount, category_id, int(input_date.timestamp()), description)

    def add_expense(self, amount, category_id=None, input_date=None, description=None):
        """
        Adds a new expense transaction for the user.

        Args:
            amount: The amount of the expense.
            category_id: The ID of the category to which the expense belongs.
            input_date: The date of the expense transaction.
            description: Additional information about the expense.
        """
        if input_date is None:
            input_date = datetime.now()
        else:
            input_date = datetime.fromtimestamp(input_date)
        add_expense(self.user_id, amount, category_id, int(input_date.timestamp()), description)

    def get_transactions(self):
        """
        Retrieves all income and expense transactions for the user.

        Returns:
            list: A list of tuples containing transaction information.
            The transactions are sorted by date in descending order.
        """
        incomes = get_all_income_transactions(self.user_id)
        expenses = get_all_expense_transactions(self.user_id)
        all_transactions = incomes + expenses

        sorted_all = sorted(all_transactions, key=lambda x: x[4], reverse=True)
        return sorted_all


    def get_transactions_with_category_names(self):
        """
        Retrieves all transactions for the user with category names.

        Returns:
            list: A list of tuples containing transaction information with category names.
        """
        transactions = self.get_transactions()
        categories = self.category_controller.get_categories()
        category_id_to_name = {category[0]: category[1] for category in categories}
        transactions_with_category_names = []
        for transaction in transactions:
            transaction_with_category_name = list(transaction)
            transaction_with_category_name[2] = category_id_to_name.get(transaction[2], "Unknown")
            transactions_with_category_names.append(tuple(transaction_with_category_name))

        return transactions_with_category_names

    def get_transactions_for_category(self, category_id):
        """
        Retrieves all income and expense transactions for a specific category.

        Args:
            category_id: The ID of the category.

        Returns:
            list: A list of tuples containing transaction information for the specified category.
        """
        incomes = get_all_income_transactions_for_category(self.user_id, category_id)
        expenses = get_all_expense_transactions_for_category(self.user_id, category_id)
        category_transactions = incomes + expenses
        return category_transactions
