import unittest
from unittest.mock import patch
from database.income import add_income, get_total_income
from database.expense import add_expense, get_total_expense
from database.database import execute_query

class TestTransactions(unittest.TestCase):

    @patch('database.income.execute_query')
    def test_add_income(self, mock_execute_query):
        user_id = 1
        amount = 100
        category_id = None
        date = None
        description = None

        add_income(user_id, amount, category_id, date, description)
        mock_execute_query.assert_called_once()

    @patch('database.expense.execute_query')
    def test_add_expense(self, mock_execute_query):
        user_id = 1
        amount = 50
        category_id = None
        date = None
        description = None

        add_expense(user_id, amount, category_id, date, description)
        mock_execute_query.assert_called_once()

    @patch('database.income.fetch_query')
    def test_get_total_income(self, mock_fetch_query):
        user_id = 1
        mock_fetch_query.return_value = [(100.0,)]

        total_income = get_total_income(user_id)
        self.assertEqual(total_income, 100)

    @patch('database.expense.fetch_query')
    def test_get_total_expense(self, mock_fetch_query):
        user_id = 1
        mock_fetch_query.return_value = [(50.0,)]

        total_expense = get_total_expense(user_id)
        self.assertEqual(total_expense, 50)

if __name__ == '__main__':
    unittest.main()
