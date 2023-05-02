## week 3
- User is able to register a new account with a username and password
- User is able to log in 
- User is able to see a smiley face 
- User is able to logout
- Implemented LoginView, RegisterView, and HomeView 
- Implemented user logic 


## week 4

- cleaned run.py 
- implemented ui_manager.py for managing the application's different views
- user is able to add expenses
- user is able to add income
- the users expense and income are saved for later login
- schema added for code

## week 5

- implemented get_transactions method to fetch and display transaction data
- extended add_income and add_expense methods in the BalanceController
- get_all_expense_transactions and all income transactions functions to retrieve all transactions for a specific user.
- modified schema
- register and login_view touch up
- home_view created treeview widget and refresh_transactions 
- got started on categories with categories controller and categories adding function


### week 6

- Get categories functions added
- Refactored code in BalanceController for better structure
- Implemented transaction controller for tranactional functionality
- Created TransactionView for income and expense management
- Updated widget layout for a cleaner UI
- Implemented function to fetch transactions with category names
- Added add_income_callback() and add_expense_callback() methods to handle data from TransactionView
- Changed the way categories are added to use the class's CategoryController instance
- Changed the way transactions are fetched and displayed in the Treeview widget
- Implemented error message for registering with existing username