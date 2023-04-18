from invoke import task

@task
def start(c):
    c.run("python3 src/run.py", pty=True)

@task
def test(c):
    c.run("pytest src")

@task
def coverage_report(c):
    c.run("pytest --cov=src --cov-report=term --cov-report=html src/tests", pty=True)

@task
def lint(c):
    c.run("pylint src", pty=True)