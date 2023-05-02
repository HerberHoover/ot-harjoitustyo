# Expense Tracker / Budgeting App

The purpose of this application is to assist users in tracking and managing their personal finances effectively. The application provides tools to track expenses and income.
The application can be used by multiple users, each managing their own financial data. The data is stored locally.

## Documents

- [Requirements Specification](./dokumentaatio/vaatimusmaarittely.md)
- [Work Log](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Architecture](./dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](./dokumentaatio/kayttoohje.md)

## Installation

- Install dependencies:

```bash
poetry install
```

- Activate the virtual environment :

```bash
poetry shell
```
- Install requirements

```bash
pip install -r ./requirements.txt
```


## Invoke tasks

- To start the application, run:

```bash
poetry run invoke start
```

- To run the tests, execute:

```bash
poetry run invoke test
```

- poetry run invoke coverage-report

```bash
poetry run invoke coverage-report
```
 
 - pylint

```bash
poetry run invoke lint
```
