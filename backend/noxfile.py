# type: ignore
import nox


@nox.session(python=["3.11"])
def precommit(session):
    session.run("pre-commit", "run", "--all-files", external=True)


@nox.session(python=["3.11"])
def lint(session) -> None:
    session.run("poetry", "run", "black", "app", external=True)
    session.run("poetry", "run", "ruff", "--fix", "app", external=True)


@nox.session(python=["3.11"])
def test(session) -> None:
    session.run("poetry", "run", "pytest", external=True)


@nox.session(python=["3.11"])
def types(session) -> None:
    session.run("poetry", "run", "mypy", "app", external=True)
