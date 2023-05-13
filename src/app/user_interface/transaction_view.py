import tkinter as tk
from tkinter import ttk, messagebox
from app.models.category_controller import CategoryController

class TransactionView(tk.Toplevel):
    """View for adding a transaction."""

    def __init__(self, user_id, transaction_type, callback, master=None):
        """
        Class constructor. Creates a new TransactionView.

        Args:
            user_id: 
                The unique ID of the user.
            transaction_type: 
                The type of transaction to be added.
            callback: 
                The callback function to be invoked upon transaction addition.
            master: 
                The parent widget, default is None.
        """
        super().__init__(master)
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.callback = callback
        self.title(f"Add {transaction_type.capitalize()}")
        self.category_controller = CategoryController(user_id)
        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets for the view."""
        self.amount_label = tk.Label(self, text="Amount:")
        self.amount_label.grid(row=0, column=0)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=0, column=1)

        self.category_label = tk.Label(self, text="Category:")
        self.category_label.grid(row=1, column=0)

        self.categories = self.category_controller.get_categories()
        category_names = [category[1] for category in self.categories]

        self.category_combobox = ttk.Combobox(self, values=category_names)
        self.category_combobox.grid(row=1, column=1)

        self.description_label = tk.Label(self, text="Description:")
        self.description_label.grid(row=2, column=0)
        self.description_entry = tk.Entry(self)
        self.description_entry.grid(row=2, column=1)

        self.add_button = tk.Button(self, text=f"Add {self.transaction_type.capitalize()}", command=self.add_transaction)
        self.add_button.grid(row=3, column=0, columnspan=2)

    def add_transaction(self):
        """
        Adds a transaction after validating the input.
        """
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            return

        category_name = self.category_combobox.get()
        description = self.description_entry.get()

        category_id = None
        for category in self.categories:
            if category[1] == category_name:
                category_id = category[0]
                break

        if not category_id:
            messagebox.showerror("Error", "Invalid category \nPlease select a category from the list")
            return

        self.callback(amount, category_id, description)
        self.destroy()
