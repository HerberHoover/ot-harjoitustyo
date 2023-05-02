import unittest
from unittest.mock import patch
from database.income import add_income, get_all_income_transactions
from database.expense import add_expense, get_all_expense_transactions
from app.models.transaction_controller import TransactionController
from app.models.category_controller import CategoryController

class TestTransactionController(unittest.TestCase):

    @patch('app.models.transaction_controller.add_income')
    def test_add_income(self, mock_add_income):
        user_id = 1
        category_controller = CategoryController(user_id)
        controller = TransactionController(user_id, category_controller)
        amount = 100
        category_id = None
        date = 420
        description = None

        controller.add_income(amount, category_id, date, description)
        mock_add_income.assert_called_once_with(user_id, amount, category_id, int(date), description)

    @patch('app.models.transaction_controller.add_expense')
    def test_add_expense(self, mock_add_expense):
        user_id = 1
        category_controller = CategoryController(user_id)
        controller = TransactionController(user_id, category_controller)
        amount = 50
        category_id = None
        date = 420
        description = None

        controller.add_expense(amount, category_id, date, description)
        mock_add_expense.assert_called_once_with(user_id, amount, category_id, int(date), description)

    @patch('app.models.transaction_controller.get_all_income_transactions')
    @patch('app.models.transaction_controller.get_all_expense_transactions')
    def test_get_transactions(self, mock_get_all_expense_transactions, mock_get_all_income_transactions):
        user_id = 1
        category_controller = CategoryController(user_id)
        controller = TransactionController(user_id, category_controller)
        mock_get_all_income_transactions.return_value = [('income', 100, 1, 1000, 1234567890)]
        mock_get_all_expense_transactions.return_value = [('expense', 50, 2, 500, 1234567900)]

        all_transactions = controller.get_transactions()

        self.assertEqual(len(all_transactions), 2)
        mock_get_all_income_transactions.assert_called_once_with(user_id)
        mock_get_all_expense_transactions.assert_called_once_with(user_id)

    @patch('app.models.transaction_controller.TransactionController.get_transactions')
    @patch('app.models.transaction_controller.CategoryController.get_categories')
    def test_get_transactions_with_category_names(self, mock_get_categories, mock_get_transactions):
        user_id = 1
        category_controller = CategoryController(user_id)
        controller = TransactionController(user_id, category_controller)
        mock_get_transactions.return_value = [('income', 100, 1, 1000, 1234567891), ('expense', 50, 2, 500, 1234567901)]
        mock_get_categories.return_value = [(1, 'Pikavippi'), (2, 'Osamaksut')]

        transactions_with_category_names = controller.get_transactions_with_category_names()

        self.assertEqual(len(transactions_with_category_names), 2)

if __name__ == '__main__':
    unittest.main()