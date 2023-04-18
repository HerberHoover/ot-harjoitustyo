import tkinter as tk
from . import LoginView, RegisterView, HomeView
from database import create_tables

class UIManager():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("400x400")

        create_tables()

        self.login_view = LoginView(self.switch_to_register, self.switch_to_home, self.root)
        self.register_view = RegisterView(self.switch_to_login, self.root)
        self.home_view = HomeView(-1, self.switch_to_login, self.root)

        self.login_view.pack(fill=tk.BOTH, expand=True)

    def switch_to_register(self):
        self.root.title("Register")
        self.login_view.pack_forget()
        self.register_view.pack(fill=tk.BOTH, expand=True)

    def switch_to_login(self):
        self.root.title("Login")
        self.register_view.pack_forget()
        self.home_view.pack_forget()
        self.login_view.pack(fill=tk.BOTH, expand=True)

    def switch_to_home(self, user_id):
        self.root.title("Home")
        self.login_view.pack_forget()
        self.home_view.user_id = user_id  # Update the user_id
        self.home_view.refresh_totals()  # Refresh the totals
        self.home_view.pack(fill=tk.BOTH, expand=True)


    def run(self):
        self.root.mainloop()