import tkinter as tk
from app.user_interface import LoginView, RegisterView, HomeView
from database import create_tables

def switch_to_register():
    root.title("Register")  # Add this line
    login_view.pack_forget()
    register_view.pack(fill=tk.BOTH, expand=True)

def switch_to_login():
    root.title("Login")  # Add this line
    register_view.pack_forget()
    home_view.pack_forget()
    login_view.pack(fill=tk.BOTH, expand=True)

def switch_to_home():
    root.title("Home")  # Add this line
    login_view.pack_forget()
    home_view.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Login")  # Add this line
    root.geometry("400x400")

    create_tables()

    login_view = LoginView(switch_to_register, switch_to_home, root)
    register_view = RegisterView(switch_to_login, root)
    home_view = HomeView(switch_to_login, root)

    login_view.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
