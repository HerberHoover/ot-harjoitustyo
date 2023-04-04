from invoke import task

@task
def start(c):
    c.run("python3 src/run.py", pty=True)

@task
def test(c):
    c.run("pytest src")

@task
def coverage_report(c):
    c.run("pytest --cov=app --cov-report html", pty=True)
