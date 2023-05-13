# CategoryTransactionsView.py
import tkinter as tk
from tkinter import ttk
from app.models.transaction_controller import TransactionController
from app.models.category_controller import CategoryController
from app.models.balance import get_category_balance
from datetime import datetime

class CategoryTransactionsView(tk.Frame):
    """View for listing transactions of a specific category."""

    def __init__(self, user_id, category, master=None, prev_view=None):
        """
        Class constructor. Creates a new CategoryTransactionsView.

        Args:
            user_id: 
                The unique ID of the user.
            category: 
                The category for which transactions are listed.
            master: 
                The parent widget, default is None.
            prev_view: 
                The previous view, default is None.
        """
        super().__init__(master)
        self.user_id = user_id
        self.category = category
        self.master = master
        self.prev_view = prev_view
        self.transaction_controller = TransactionController(self.user_id, CategoryController(self.user_id))
        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets for the view."""
        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.grid(row=0, column=0)

        balance = get_category_balance(self.user_id, self.category[0])
        balance_label = tk.Label(self, text=f"Balance: {balance}")
        balance_label.grid(row=3, column=0)

        style = ttk.Style()
        style.configure('Treeview', show='headings')

        self.transactions_tree = ttk.Treeview(self, columns=('Type', 'Amount', 'Date', 'Description'), show='headings')
        self.transactions_tree.heading('Type', text='Type')
        self.transactions_tree.heading('Amount', text='Amount')
        self.transactions_tree.heading('Date', text='Date')
        self.transactions_tree.heading('Description', text='Description')
        self.transactions_tree.grid(row=4, column=0, padx=10, pady=10)

        self.focus_set()

        self.refresh_transactions()

    def refresh_transactions(self):
        """
        Refreshes the transactions list by removing the existing entries and loading new ones from the database.
        """
        self.transactions_tree.delete(*self.transactions_tree.get_children())
        if self.user_id == -1:
            return

        transactions = self.transaction_controller.get_transactions_for_category(self.category[0])
        for transaction in transactions:
            if transaction[4] is not None:
                date_str = datetime.fromtimestamp(transaction[4]).strftime('%Y-%m-%d')
            else:
                date_str = 'N/A'
            self.transactions_tree.insert('', 0, values=(transaction[6], transaction[3], date_str, transaction[5]))

    def go_back(self):
        """
        Go back to the previous view.
        """
        if self.prev_view:
            self.pack_forget()
            self.prev_view.pack()
