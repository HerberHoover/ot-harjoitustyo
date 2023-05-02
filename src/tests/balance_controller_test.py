import unittest
from unittest.mock import patch
from app.models.balance_controller import BalanceController
from app.models.balance import get_balance

class TestBalanceController(unittest.TestCase):

    @patch('app.models.balance_controller.get_total_income')
    @patch('app.models.balance_controller.get_total_expense')
    @patch('app.models.balance_controller.get_balance')
    def test_get_totals(self, mock_get_balance, mock_get_total_expense, mock_get_total_income):
        user_id = 420
        controller = BalanceController(user_id)
        mock_get_total_income.return_value = 1000
        mock_get_total_expense.return_value = 500
        mock_get_balance.return_value = 500

        total_income, total_expense, balance = controller.get_totals()

        print("Total Income:", total_income)
        print("Total Expense:", total_expense)
        print("Balance:", balance)

        self.assertEqual(total_income, 1000)
        self.assertEqual(total_expense, 500)
        self.assertEqual(balance, 500)

        mock_get_total_income.assert_called_once_with(user_id)
        mock_get_total_expense.assert_called_once_with(user_id)
        mock_get_balance.assert_called_once_with(user_id)


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
