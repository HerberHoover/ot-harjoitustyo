from tkinter import messagebox
from database.user import verify_user, create_user

def login(username, password):
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return False

    if verify_user(username, password):
        messagebox.showinfo("Success", "You have successfully logged in.")
        return True

    messagebox.showerror("Error", "Invalid username or password.")
    return False

def register(username, password, confirm_password):
    if not username or not password or not confirm_password:
        messagebox.showerror("Error", "Please enter all fields.")
        return False

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return False

    create_user(username, password)
    messagebox.showinfo("Success", "Registration successful.")
    return True
