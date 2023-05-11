import tkinter as tk
from tkinter import ttk, simpledialog
from database.expense import add_expense, get_total_expense
from database.income import add_income, get_total_income
from app.models.balance import get_balance
from app.models.balance_controller import BalanceController
from app.models.category_controller import CategoryController
from app.models.transaction_controller import TransactionController
from datetime import datetime
from tkinter import messagebox
from .transaction_view import TransactionView
from .category_view import CategoryView

class HomeView(tk.Frame):
    def __init__(self, user_id, switch_to_login, master=None):
        super().__init__(master)
        self.master = master
        self.user_id = user_id
        self.balance_controller = BalanceController(user_id)
        self.category_controller = CategoryController(user_id)
        self.transaction_controller = TransactionController(user_id, self.category_controller)
        self.switch_to_login = switch_to_login
        self.create_widgets()

    def create_widgets(self):
        self.logout_button = tk.Button(self, text="Logout", command=self.logout)
        self.logout_button.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.add_income_button = tk.Button(self, text="Add Income", command=self.add_income)
        self.add_income_button.grid(row=2, column=0, padx=10, pady=10)

        self.add_expense_button = tk.Button(self, text="Add Expense", command=self.add_expense)
        self.add_expense_button.grid(row=3, column=0, padx=10, pady=10)

        self.add_category_button = tk.Button(self, text="Add Category", command=self.add_category)
        self.add_category_button.grid(row=4, column=0, padx=10, pady=10)

        self.total_income_label = tk.Label(self, text="Total Income:")
        self.total_income_label.grid(row=2, column=1, padx=10, pady=10)
        self.total_income_value = tk.StringVar()
        self.total_income_value.set("0")
        self.total_income_display = tk.Label(self, textvariable=self.total_income_value)
        self.total_income_display.grid(row=2, column=2, padx=10, pady=10)
        self.total_income_display.config(font=("TkDefaultFont", 14))

        self.total_expense_label = tk.Label(self, text="Total Expenses:")
        self.total_expense_label.grid(row=3, column=1, padx=10, pady=10)
        self.total_expense_value = tk.StringVar()
        self.total_expense_value.set("0")
        self.total_expense_display = tk.Label(self, textvariable=self.total_expense_value)
        self.total_expense_display.grid(row=3, column=2, padx=10, pady=10)
        self.total_expense_display.config(font=("TkDefaultFont", 14))

        self.balance_label = tk.Label(self, text="Balance:")
        self.balance_label.grid(row=4, column=1, padx=10, pady=10)
        self.balance_value = tk.StringVar()
        self.balance_value.set("0")
        self.balance_display = tk.Label(self, textvariable=self.balance_value)
        self.balance_display.grid(row=4, column=2, padx=10, pady=10)
        self.balance_display.config(font=("TkDefaultFont", 14))

        self.view_categories_button = tk.Button(self, text="View Categories", command=self.view_categories)
        self.view_categories_button.grid(row=5, column=0, padx=10, pady=10)

        style = ttk.Style()
        style.configure('Treeview', show='headings')

        self.transactions_tree = ttk.Treeview(self, columns=('Type', 'Amount', 'Category', 'Date', 'Description'), show='headings')
        self.transactions_tree.heading('Type', text='Type')
        self.transactions_tree.heading('Amount', text='Amount')
        self.transactions_tree.heading('Category', text='Category')
        self.transactions_tree.heading('Date', text='Date')
        self.transactions_tree.heading('Description', text='Description')
        self.transactions_tree.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

        self.add_categories_first_label = tk.Label(self, text="*NB: Add categories first*", font=("TkDefaultFont", 10))
        self.add_categories_first_label.grid(row=13, column=0, columnspan=1, padx=0, pady=10)

        self.refresh_totals()
        self.refresh_transactions()

    def refresh_totals(self):
        if self.user_id == -1:
            return 

        total_income, total_expense, balance = self.balance_controller.get_totals()

        self.total_income_value.set("{:.2f}".format(total_income))
        self.total_expense_value.set("{:.2f}".format(total_expense))
        self.balance_value.set("{:.2f}".format(balance))

    def refresh_transactions(self):
        self.transactions_tree.delete(*self.transactions_tree.get_children())
        if self.user_id == -1:
            return

        transactions = self.transaction_controller.get_transactions_with_category_names()
        for transaction in transactions:
            if transaction[4] is not None:
                date_str = datetime.fromtimestamp(transaction[4]).strftime('%Y-%m-%d')
            else:
                date_str = 'N/A'
            self.transactions_tree.insert('', 'end', values=(transaction[6], transaction[3], transaction[2], date_str, transaction[5]))

    def add_income(self):
        transaction_view = TransactionView(self.user_id, "income", self.add_income_callback)
        transaction_view.mainloop()

    def add_expense(self):
        transaction_view = TransactionView(self.user_id, "expense", self.add_expense_callback)
        transaction_view.mainloop()

    def add_income_callback(self, amount, category, description):
        self.transaction_controller.add_income(amount=amount, category_id=category, description=description)
        self.refresh_totals()
        self.refresh_transactions()

    def add_expense_callback(self, amount, category, description):
        self.transaction_controller.add_expense(amount=amount, category_id=category, description=description)
        self.refresh_totals()
        self.refresh_transactions()

    def logout(self):
        self.pack_forget()
        self.switch_to_login()
      
    def add_category(self):
        category_name = simpledialog.askstring("Add Category", "Enter new category name:", parent=self)
        if category_name:
            category_controller = CategoryController(self.user_id)
            category_controller.add_category(category_name)

    def view_categories(self):
        self.pack_forget()
        categories_view = CategoryView(self.user_id, self.master, self)
        categories_view.pack()
