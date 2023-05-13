# User Manual


### Newest release
[Newest release](https://github.com/HerberHoover/ot-harjoitustyo/releases/tag/loppupalautus)

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

From the login view, you can navigate to the new user registration view by clicking the "Register" button.

Create a new user by entering the required information in the input fields and clicking the "Register" button.

If the user registration is successful, you can redirect yourself back to login by pressing "Back to Login."



## Creating Categories

To create a new category, click the "Add Category" button. Enter the desired category name in the input field and click the "OK" button.

Your newly created category will now appear in the list of available categories which can be assigned to transactions.

## Adding Transactions

To add a transaction, click the "Add Income" or "Add Expense" button. 
A form will appear where you can enter the transaction details:

Amount: Enter the transaction amount.
Category: Choose an existing category to assign to the transaction.

Description (optional): Add a description for the transaction.

Click the "Add I/E" button to add the transaction to your records. The transaction will now appear in the list of transactions organized by date.

## Viewing Transactions by Category

To view transactions by category, click the "View Categories" button. This will navigate you to the categories page, where you can see all the categories you've created.

To view transactions from a specific category, click the button labeled with the name of the category you're interested in. This will display all transactions linked to that category.

## Other functionality

To go back from viewing categories and category-specific transactions, click on the "Back" button.

To log out from the application, click the "Logout" button on the application's home screen.