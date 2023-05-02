### User Manual

Will add pictures in the future
### Newest release
[Newest release](https://github.com/HerberHoover/ot-harjoitustyo)

## Installation

- Install dependencies:

```bash
poetry install
```

- Activate the virtual environment:

```bash
poetry shell
```
- Install requirements

```bash
pip install -r ./requirements.txt
```


## Starting the application

- To start the application, run:

```bash
poetry run invoke start
```

## Logging In


To log in, enter an existing username and password in the input fields and click the "Login" button

## Registering
From the login view, you can navigate to the new user registration view by clicking the "Register" button

Create a new user by entering the required information in the input fields and clicking the "Register" button

If the user registration is successful, you can redirect yourself back to login by pressing "Back to Login"



## Creating Categories

To create a new category, click the "Add Category" button. Enter the desired category name in the input field and click the "OK" button.

Your newly created category will now appear in the list of available categories, which can be assigned to transactions.

## Adding Transactions

To add a transaction, click "Add Income" or "Add Expense" button. 
A form will appear where you can enter the transaction details:

Amount: Enter the transaction amount.
Category: Choose an existing category to assign to the transaction.

Description (optional): Add a description for the transaction.

Click the "Add I/E" button to add the transaction to your records. The transaction will now appear in the list of transactions, organized by date.