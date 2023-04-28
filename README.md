# Expense Tracker / Budgeting App




## Documents

- [Requirements Specification](./dokumentaatio/vaatimusmaarittely.md)
- [Work Log](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Architecture](./dokumentaatio/arkkitehtuuri.md)

## Installation

- Install dependencies:

```bash
poetry install
```

- Activate the virtual environment :

```bash
poetry shell
```

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