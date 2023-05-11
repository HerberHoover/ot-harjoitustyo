# CategoryView.py
import tkinter as tk
from tkinter import messagebox
from app.models.category_controller import CategoryController
from .category_transactions_view import CategoryTransactionsView

class CategoryView(tk.Frame):
    def __init__(self, user_id, master=None, prev_view=None):
        super().__init__(master)
        self.user_id = user_id
        self.master = master
        self.prev_view = prev_view
        self.category_controller = CategoryController(user_id)
        self.create_widgets()

    def create_widgets(self):
        self.categories = self.category_controller.get_categories()

        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.grid(row=0, column=0)

        tk.Label(self).grid(row=1, column=0)

        for i, category in enumerate(self.categories):
            category_name = category[1]
            category_button = tk.Button(self, text=category_name, width=20, command=self.create_view_category_command(category))
            category_button.grid(row=i+2, column=0)

    def create_view_category_command(self, category):
        def view_category():
            self.pack_forget()
            transactions_view = CategoryTransactionsView(self.user_id, category, self.master, self)
            transactions_view.pack()
        return view_category

    def view_category(self, category):
        self.pack_forget()
        transactions_view = CategoryTransactionsView(self.user_id, category, self.master, self)
        transactions_view.pack()

    def go_back(self):
        if self.prev_view:
            self.pack_forget()
            self.prev_view.pack()



"""         # CategoryView.py
import tkinter as tk
from tkinter import messagebox
from app.models.category_controller import CategoryController
from .category_transactions_view import CategoryTransactionsView

class CategoryView(tk.Frame):
    def __init__(self, user_id, master=None, prev_view=None):
        super().__init__(master)
        self.user_id = user_id
        self.master = master
        self.prev_view = prev_view  # keep a reference to the previous view
        self.category_controller = CategoryController(user_id)
        self.create_widgets()

    def create_widgets(self):
        self.categories = self.category_controller.get_categories()

        # Create a back button
        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.grid(row=0, column=0)
        
        for i, category in enumerate(self.categories):
            category_name = category[1]
            category_button = tk.Button(self, text=category_name, command=lambda c=category: self.view_category(c))
            category_button.grid(row=i+1, column=0)  # Adjust the row index to leave room for the back button

    def view_category(self, category):
        self.pack_forget()  # hide the current view
        transactions_view = CategoryTransactionsView(self.user_id, category, self.master, self)
        transactions_view.pack()  # show the new view

    def go_back(self):
        if self.prev_view:
            self.pack_forget()
            self.prev_view.pack()

"""