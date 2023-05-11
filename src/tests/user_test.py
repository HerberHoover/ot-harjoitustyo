import unittest
from unittest.mock import patch
from database.user import create_user, get_user_by_username, verify_user
from database.database import execute_query, fetch_query
import hashlib

class TestUser(unittest.TestCase):

    @patch('database.user.get_user_by_username')
    @patch('database.user.execute_query')
    def test_create_user(self, mock_execute_query, mock_get_user_by_username):
        mock_get_user_by_username.return_value = None
        mock_execute_query.return_value = True
        username = "username"
        password = "password"
        
        result = create_user(username, password)
        self.assertTrue(result)
        mock_execute_query.assert_called_once_with(''' INSERT INTO users(username, password_hash) VALUES(?,?) ''', (username, hashlib.sha256(password.encode()).hexdigest()))

    @patch('database.user.fetch_query')
    def test_get_user_by_username(self, mock_fetch_query):
        user_id = 4
        username = "username"
        password = "password"
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        mock_fetch_query.return_value = [(user_id, username, password_hash)]
        
        user = get_user_by_username(username)
        self.assertEqual(user, (user_id, username, password_hash))
        mock_fetch_query.assert_called_once_with(''' SELECT * FROM users WHERE username = ? ''', (username,))

    @patch('database.user.get_user_by_username')
    def test_verify_user(self, mock_get_user_by_username):
        user_id = 4
        username = "username"
        password = "password"
        mock_get_user_by_username.return_value = (user_id, username, hashlib.sha256(password.encode()).hexdigest())
        
        is_verified = verify_user(username, password)
        self.assertTrue(is_verified)
        mock_get_user_by_username.assert_called_once_with(username)

    @patch('database.user.get_user_by_username')
    def test_verify_user_wrong_password(self, mock_get_user_by_username):
        user_id = 4
        username = "username"
        password = "password"
        mock_get_user_by_username.return_value = (user_id, username, hashlib.sha256("wrong_password".encode()).hexdigest())
        
        is_verified = verify_user(username, password)
        self.assertFalse(is_verified)
        mock_get_user_by_username.assert_called_once_with(username)



if __name__ == '__main__':
    unittest.main()