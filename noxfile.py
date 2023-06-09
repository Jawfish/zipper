# type: ignore
import nox


@nox.session(python=["3.11"])
def lint(session) -> None:
    session.run("poetry", "run", "black", "backend", external=True)
    session.run("poetry", "run", "ruff", "--fix", "backend", external=True)


@nox.session(python=["3.11"])
def test(session) -> None:
    session.run("poetry", "run", "pytest", external=True)


@nox.session(python=["3.11"])
def types(session) -> None:
    session.run("poetry", "run", "mypy", "backend", external=True)
