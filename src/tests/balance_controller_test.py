import unittest
from unittest.mock import patch
from app.models.balance_controller import BalanceController
from database.income import add_income, get_total_income, get_all_income_transactions
from database.expense import add_expense, get_total_expense, get_all_expense_transactions
from app.models.balance import get_balance

class TestBalanceController(unittest.TestCase):

    @patch('app.models.balance_controller.add_income')
    def test_add_income(self, mock_add_income):
        user_id = 1
        controller = BalanceController(user_id)
        amount = 100
        category_id = None
        date = 420
        description = None

        controller.add_income(amount, category_id, date, description)
        mock_add_income.assert_called_once()

    @patch('app.models.balance_controller.add_expense')
    def test_add_expense(self, mock_add_expense):
        user_id = 1
        controller = BalanceController(user_id)
        amount = 50
        category_id = None
        date = 420
        description = None

        controller.add_expense(amount, category_id, date, description)
        mock_add_expense.assert_called_once()

    @patch('app.models.balance_controller.get_total_income')
    @patch('app.models.balance_controller.get_total_expense')
    @patch('app.models.balance_controller.get_balance')
    def test_get_totals(self, mock_get_balance, mock_get_total_expense, mock_get_total_income):
        user_id = 1
        controller = BalanceController(user_id)
        mock_get_total_income.return_value = 100
        mock_get_total_expense.return_value = 50
        mock_get_balance.return_value = 50

        total_income, total_expense, balance = controller.get_totals()

        self.assertEqual(total_income, 100)
        self.assertEqual(total_expense, 50)
        self.assertEqual(balance, 50)

    @patch('app.models.balance_controller.get_all_income_transactions')
    @patch('app.models.balance_controller.get_all_expense_transactions')
    def test_get_transactions(self, mock_get_all_expense_transactions, mock_get_all_income_transactions):
        user_id = 1
        controller = BalanceController(user_id)

        mock_get_all_income_transactions.return_value = [('income', 100, None, None, 1234567890)]
        mock_get_all_expense_transactions.return_value = [('expense', 50, None, None, 1234567900)]

        all_transactions = controller.get_transactions()

        self.assertEqual(len(all_transactions), 2)
        self.assertIn(('income', 100, None, None, 1234567890), all_transactions)
        self.assertIn(('expense', 50, None, None, 1234567900), all_transactions)
        self.assertTrue(all_transactions[0][4] >= all_transactions[1][4])


    @patch('app.models.balance.get_total_income')
    @patch('app.models.balance.get_total_expense')
    def test_get_balance(self, mock_get_total_expense, mock_get_total_income):
        user_id = 1

        mock_get_total_income.return_value = 1000
        mock_get_total_expense.return_value = 500

        balance = get_balance(user_id)

        self.assertEqual(balance, 500)
        mock_get_total_income.assert_called_once_with(user_id)
        mock_get_total_expense.assert_called_once_with(user_id)


if __name__ == '__main__':
    unittest.main()
