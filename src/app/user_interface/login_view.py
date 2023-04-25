import tkinter as tk
from tkinter import messagebox
from database.user import verify_user, get_user_by_username
from app.models.user_logic import login, register



class LoginView(tk.Frame):
    def __init__(self, switch_to_register, switch_to_home, master=None):
        super().__init__(master)
        self.master = master
        self.switch_to_register = switch_to_register
        self.switch_to_home = switch_to_home
        self.create_widgets()


    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=2, padx=10, pady=10)

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=2, padx=10, pady=10)

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)


    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user_found = verify_user(username, password)

        if user_found:
            user_data = get_user_by_username(username) 
            self.pack_forget()
            self.switch_to_home(user_id=user_data[0]) 
        else:
            messagebox.showerror("Error", "Invalid username or password.")



    def register(self):
        self.pack_forget()
        self.switch_to_register()
