import tkinter as tk
from database.expense import add_expense, get_total_expense
from database.income import add_income, get_total_income
from app.models.balance import get_balance
from app.models.balance_controller import BalanceController




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

        self.refresh_totals()


    def refresh_totals(self):
        if self.user_id == -1:
            return 

        total_income, total_expense, balance = self.balance_controller.get_totals()

        self.total_income_value.set("{:.2f}".format(total_income))
        self.total_expense_value.set("{:.2f}".format(total_expense))
        self.balance_value.set("{:.2f}".format(balance))


    def add_income(self):
        amount = float(self.income_entry.get())
        self.balance_controller.add_income(amount)
        self.refresh_totals()

    def add_expense(self):
        amount = float(self.expense_entry.get())
        self.balance_controller.add_expense(amount)
        self.refresh_totals()


    def logout(self):
        self.pack_forget()
        self.switch_to_login()
      



        