# ui_manager.py
import tkinter as tk
from . import LoginView, RegisterView, HomeView, CategoryView
from database import create_tables

class UIManager:
    """
    A class to manage the user interface of the application.

    Attributes:
        root (tk.Tk): The root Tkinter object for the application.
        login_view (LoginView): The login view object.
        register_view (RegisterView): The register view object.
        home_view (HomeView): The home view object.
    """

    def __init__(self):
        """
        Initializes a new UIManager instance.
        """
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("1030x650")

        create_tables()

        self.login_view = LoginView(self.switch_to_register, self.switch_to_home, self.root)
        self.register_view = RegisterView(self.switch_to_login, self.root)
        self.home_view = HomeView(-1, self.switch_to_login, self.root)

        self.login_view.pack(fill=tk.BOTH, expand=True)

    def switch_to_register(self):
        """
        Switches the view to the Register view.
        """
        self.root.title("Register")
        self.login_view.pack_forget()
        self.register_view.pack(fill=tk.BOTH, expand=True)

    def switch_to_login(self):
        """
        Switches the view to the Login view.
        """
        self.root.title("Login")
        self.register_view.pack_forget()
        self.home_view.pack_forget()
        self.login_view.pack(fill=tk.BOTH, expand=True)

    def switch_to_home(self, user_id):
        """
        Switches the view to the Home view.

        Args:
            user_id (int): The user ID for which the home view is displayed.
        """
        self.root.title("Home")
        self.login_view.pack_forget()

        self.home_view = HomeView(user_id, self.switch_to_login, self.root)
        self.home_view.refresh_totals()
        self.home_view.refresh_transactions()
        self.home_view.pack(fill=tk.BOTH, expand=True)

    def run(self):
        """
        Starts the Tkinter main loop for the application.
        """
        self.root.mainloop()
