import unittest
from unittest.mock import patch, mock_open, MagicMock
from database import create_database, database

class TestDatabase(unittest.TestCase):
    @patch('database.database.sqlite3.connect')
    def test_execute_query(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        database.execute_query('SELECT * FROM table')

        mock_cursor.execute.assert_called_once_with('SELECT * FROM table', ())

    @patch('database.database.sqlite3.connect')
    def test_fetch_query(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        database.fetch_query('SELECT * FROM table')

        mock_cursor.execute.assert_called_once_with('SELECT * FROM table', ())
        mock_cursor.fetchall.assert_called_once()

    @patch('database.create_database.read_sql_file', return_value='CREATE TABLE test;')
    @patch('database.create_database.execute_query')
    @patch('database.create_database.create_connection')
    def test_create_tables(self, mock_create_connection, mock_execute_query, mock_read_sql_file):
        create_database.create_tables()

        mock_read_sql_file.assert_called_once()
        mock_execute_query.assert_called_once_with('CREATE TABLE test')