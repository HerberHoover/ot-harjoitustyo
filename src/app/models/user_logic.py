from tkinter import messagebox
from database.user import verify_user, create_user

def login(username, password):
    """Logs in the user with the provided username and password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        bool: True if the login is successful, False otherwise.
    """
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return False

    if verify_user(username, password):
        messagebox.showinfo("Success", "You have successfully logged in.")
        return True

    messagebox.showerror("Error", "Invalid username or password.")
    return False

def register(username, password, confirm_password):
    """Registers a new user with the provided username and password.

    Args:
        username (str): The desired username of the new user.
        password (str): The desired password of the new user.
        confirm_password (str): The confirmation of the desired password.

    Returns:
        bool: True if the registration is successful, False otherwise.
    """
    if not username or not password or not confirm_password:
        messagebox.showerror("Error", "Please enter all fields.")
        return False

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return False

    if create_user(username, password):
        messagebox.showinfo("Success", "Registration successful.")
        return True

    messagebox.showerror("Error", "Username is already in use.")
    return False
