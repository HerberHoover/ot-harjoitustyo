## Architectural Description

The architecture of the system is designed around a three-tiered layered structure, following the principles of separation of concerns and modularity. 

## Rudimentary UML Class Diagram
![UML Class diagram](./kuvat/classdiagramnoob.png)

### Models

This directory contains the core application logic of the application. The files in this directory implement functionality related to user authentication, balance calculation, transactions, and categories.

- The user_logic.py module handles user registration and login.

- The balance.py module provides a function to calculate the user's balance.

- The balance_controller.py, transaction_controller.py, and category_controller.py modules define classes responsible for coordinating specific operations and interactions between the user interface, the underlying application logic, and the database.

### User Interface

This directory contains the user interface code implemented using the tkinter library. It has separate views for registration, login, and the home screen, along with a UI manager, categories view, transaction view and a transactions by category view.

- The modules register_view.py, login_view.py, home_view.py, category_view.py, category_transaction_view.py, and transaction_view.py respectively handle views for user registration, login, home screen, category, category transactions, and transaction management. 

- The ui_manager.py module is responsible for managing the overall UI structure and navigation,

### Database

This directory contains the code to interact with the SQLite database. It defines the schema, creates the database and tables, and provides query execution and table management functionality.

- The create_database.py module contains code to create the database and its tables based on the defined schema.

- The user.py, income.py, expense.py, and categories.py modules provide functionality for managing the respective database tables. 

- The database.py module provides functions for connecting to the SQLite database, executing queries, and fetching results. It bridges the application logic and the database, ensuring that the data is correctly stored and retrieved.



## Sequence diagrams

### This sequence diagram represents the flow of adding income and expense transactions. 

```mermaid
sequenceDiagram
  participant User_Interface
  participant TransactionController
  participant Database
  User_Interface->>TransactionController: add_income()
  TransactionController->>Database: add_income()
  User_Interface->>TransactionController: add_expense()
  TransactionController->>Database: add_income()
```

### This sequence diagram represents the flow of getting category specific transactions.


```mermaid
sequenceDiagram
  participant User_Interface
  participant TransactionController
  participant Database
  participant CategoryController

  User_Interface->>TransactionController: get_transactions_with_category_names()
  TransactionController->>TransactionController: get_transactions()
  TransactionController->>Database: get_all_income_transactions()
  Database-->>TransactionController: Return income transactions 
  TransactionController->>Database: get_all_expense_transactions()
  Database-->>TransactionController: Return expense transactions
  TransactionController->>CategoryController: get_categories()
  CategoryController->>Database: get_categories()
  Database-->>CategoryController: Return categories
  CategoryController-->>TransactionController: Return categories
  TransactionController-->>User_Interface: Return transactions with category names
```

### More accurate class diagram

![UML Class diagram](./kuvat/classdiagram.png)