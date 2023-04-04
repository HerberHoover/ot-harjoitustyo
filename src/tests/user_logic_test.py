import unittest
from unittest.mock import patch
from app.models.user_logic import login, register
from database.user import verify_user, create_user

class TestUserLogic(unittest.TestCase):

    @patch('app.models.user_logic.messagebox')
    def test_login_missing_username(self, mock_messagebox):
        result = login("", "password")
        self.assertFalse(result)
        mock_messagebox.showerror.assert_called_with("Error", "Please enter both username and password.")

    @patch('app.models.user_logic.verify_user')
    @patch('app.models.user_logic.messagebox')
    def test_login_valid_user(self, mock_messagebox, mock_verify_user):
        mock_verify_user.return_value = True
        result = login("username", "password")
        self.assertTrue(result)
        mock_messagebox.showinfo.assert_called_with("Success", "You have successfully logged in.")

    @patch('app.models.user_logic.verify_user')
    @patch('app.models.user_logic.messagebox')
    def test_login_invalid_user(self, mock_messagebox, mock_verify_user):
        mock_verify_user.return_value = False
        result = login("username", "password")
        self.assertFalse(result)
        mock_messagebox.showerror.assert_called_with("Error", "Invalid username or password.")

    @patch('app.models.user_logic.messagebox')
    def test_register_missing_fields(self, mock_messagebox):
        result = register("username", "", "")
        self.assertFalse(result)
        mock_messagebox.showerror.assert_called_with("Error", "Please enter all fields.")

    @patch('app.models.user_logic.messagebox')
    def test_register_password_mismatch(self, mock_messagebox):
        result = register("username", "password", "different_password")
        self.assertFalse(result)
        mock_messagebox.showerror.assert_called_with("Error", "Passwords do not match.")

    @patch('app.models.user_logic.create_user')
    @patch('app.models.user_logic.messagebox')
    def test_register_successful_registration(self, mock_messagebox, mock_create_user):
        result = register("username", "password", "password")
        self.assertTrue(result)
        mock_create_user.assert_called_with("username", "password")
        mock_messagebox.showinfo.assert_called_with("Success", "Registration successful.")

if __name__ == '__main__':
    unittest.main()
