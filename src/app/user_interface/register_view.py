import tkinter as tk
from tkinter import messagebox
from database.user import create_user
from app.models.user_logic import register

class RegisterView(tk.Frame):
    def __init__(self, switch_to_login, master=None):
        super().__init__(master)
        self.master = master
        self.switch_to_login = switch_to_login
        self.create_widgets()


    def create_widgets(self):
        self.master.title("Register")

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.confirm_password_label = tk.Label(self, text="Confirm Password:")
        self.confirm_password_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.grid(row=3, column=1, padx=10, pady=10, sticky=tk.E)

        self.back_button = tk.Button(self, text="Back to Login", command=self.back_to_login)
        self.back_button.grid(row=4, column=1, padx=10, pady=10, sticky=tk.E)
    
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if register(username, password, confirm_password):
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.confirm_password_entry.delete(0, tk.END)

    def back_to_login(self):
        self.pack_forget()
        self.switch_to_login()

