# pls.zip

<https://pls.zip> is a webapp where users can upload files to receive downloadable an archive of them. The application is developed using the Python FastAPI framework.

## Getting Started

### Prerequisites

- Python 3.11
- [Poetry](https://python-poetry.org/) package manager

### Installation

1. Clone the repository

    ```bash
    git clone https://github.com/your_username_/pls.zip.git
    cd pls.zip
    ```

2. Install dependencies using Poetry

    ```bash
    poetry install
    ```

3. Start the application

    ```bash
    poetry run app
    ```

## Configuration

Application settings are loaded from environment variables which are set in a `.env` file. An example `.env` file would look like this:

```ini
FILE_DIRECTORY=./files
ZIP_DIRECTORY=./zipped_files
USE_SYS_TMP=true

```

- `FILE_DIRECTORY`: The directory where uploaded files are temporarily stored.
- `ZIP_DIRECTORY`: The directory where zipped files are stored.
- `USE_SYS_TMP`: Whether or not to use the system's temporary directory for file storage.

## Contributing

### TL;DR

```bash
# clone and make changes
git clone https://github.com/pls-zip/pls.zip.git
cd pls.zip
poetry install

# create a new branch
git checkout -b my-feature

# run app
poetry run app

# run checks
poetry run nox

# commit changes
git add .
git commit -m "tag: short description"

# push changes
git push origin my-feature
```

### Coding Standards

The project adheres to a set of coding standards to ensure code quality and consistency. We use a variety of tools to enforce these standards:

- Code is formatted with `black`
- Static type checking is performed with `mypy`
- Code is linted with `ruff`

Before you commit your changes, please ensure your code adheres to these standards. For your convenience, all of the necessary checks, including tests, are included in the `noxfile.py` file. To run all of the checks, simply run:

```bash
poetry run nox
```

### Testing

We use `pytest` for our testing framework. To ensure your changes do not break existing functionality, please write tests for any new features or changes and ensure all tests pass before submitting your changes.

To run the tests:

```bash
poetry run pytest
```

Or, you can use `nox` to run the tests along with the other checks:

```bash
poetry run nox
```

### Committing Your Changes

We follow a conventional commit style, so your commit message should look like this:

```markdown
feat: add new feature
fix: fix a bug
test: add tests
docs: update documentation
chore: make a chore change
build: make a build change
refactor: make a refactor change
```

They should look something like this:

```bash
git add .
git commit -m "tag: short description"
```

#### Pre-Commit Hooks

We use pre-commit hooks to ensure code quality and run some checks before each commit. The hooks enforce the conventional commit style. These are run when you run `nox`, but if you'd like to run them on their own, you can do so with:

```bash
poetry run pre-commit run --all-files
```

You can also have them run automatically on commit by installing the pre-commit hooks:

```bash
poetry run pre-commit install
```

## License

Distributed under the MIT License. See `LICENSE` for more information.
