import tkinter as tk
from tkinter import ttk, simpledialog
from database.expense import add_expense, get_total_expense
from database.income import add_income, get_total_income
from app.models.balance import get_balance
from app.models.balance_controller import BalanceController
from app.models.category_controller import CategoryController
from datetime import datetime
from tkinter import messagebox



class HomeView(tk.Frame):
    def __init__(self, user_id, switch_to_login, master=None):
        super().__init__(master)
        self.master = master
        self.user_id = user_id
        self.balance_controller = BalanceController(user_id)
        self.switch_to_login = switch_to_login
        self.create_widgets()

    def create_widgets(self):
        self.home_label = tk.Label(self, text=":-)")
        self.home_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.logout_button = tk.Button(self, text="Logout", command=self.logout)  
        self.logout_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)


        self.income_label = tk.Label(self, text="Income:")
        self.income_label.grid(row=2, column=0)
        self.income_entry = tk.Entry(self)
        self.income_entry.grid(row=2, column=1)

        self.expense_label = tk.Label(self, text="Expense:")
        self.expense_label.grid(row=3, column=0)
        self.expense_entry = tk.Entry(self)
        self.expense_entry.grid(row=3, column=1)

        self.add_income_button = tk.Button(self, text="Add Income", command=self.add_income)
        self.add_income_button.grid(row=2, column=2)

        self.add_expense_button = tk.Button(self, text="Add Expense", command=self.add_expense)
        self.add_expense_button.grid(row=3, column=2)

        self.total_income_label = tk.Label(self, text="Total Income:")
        self.total_income_label.grid(row=4, column=0)
        self.total_income_value = tk.StringVar()
        self.total_income_value.set("0")
        self.total_income_display = tk.Label(self, textvariable=self.total_income_value)
        self.total_income_display.grid(row=4, column=1)

        self.total_expense_label = tk.Label(self, text="Total Expenses:")
        self.total_expense_label.grid(row=5, column=0)
        self.total_expense_value = tk.StringVar()
        self.total_expense_value.set("0")
        self.total_expense_display = tk.Label(self, textvariable=self.total_expense_value)
        self.total_expense_display.grid(row=5, column=1)

        self.balance_label = tk.Label(self, text="Balance:")
        self.balance_label.grid(row=6, column=0)
        self.balance_value = tk.StringVar()
        self.balance_value.set("0")
        self.balance_display = tk.Label(self, textvariable=self.balance_value)
        self.balance_display.grid(row=6, column=1)

        self.add_category_button = tk.Button(self, text="Add Category", command=self.add_category)
        self.add_category_button.grid(row=8, column=0, padx=10, pady=10)


        self.refresh_totals()

        self.transactions_tree = ttk.Treeview(self, columns=('Type', 'Amount', 'Category', 'Date', 'Description'))
        self.transactions_tree.heading('#0', text='ID')
        self.transactions_tree.heading('Type', text='Type')
        self.transactions_tree.heading('Amount', text='Amount')
        self.transactions_tree.heading('Category', text='Category')
        self.transactions_tree.heading('Date', text='Date')
        self.transactions_tree.heading('Description', text='Description')
        self.transactions_tree.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

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

        transactions = self.balance_controller.get_transactions()
        for transaction in transactions:
            if transaction[4] is not None:
                date_str = datetime.fromtimestamp(transaction[4]).strftime('%Y-%m-%d')
            else:
                date_str = 'N/A'
            self.transactions_tree.insert('', 'end', text=transaction[0], values=(transaction[6], transaction[3], transaction[1], date_str, transaction[5]))


    def add_income(self):
        try:
            amount = float(self.income_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            return
        self.balance_controller.add_income(amount)
        self.refresh_totals()
        self.refresh_transactions()

    def add_expense(self):
        try:
            amount = float(self.expense_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            return
        self.balance_controller.add_expense(amount)
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

        