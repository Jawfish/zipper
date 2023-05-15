# type: ignore
import nox


@nox.session(python=["3.11.3"])
def tests(session) -> None:
    session.run("poetry", "run", "pre-commit", "run", "--all-files", external=True)
    session.run("poetry", "run", "black", "app", external=True)
    session.run("poetry", "run", "ruff", "--fix", "app", external=True)
    session.run("poetry", "run", "mypy", "app", external=True)
    session.run("poetry", "run", "pytest", external=True)
