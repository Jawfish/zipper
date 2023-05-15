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

## Testing

Run the tests using pytest.

```bash
poetry run pytest
```

## License

Distributed under the MIT License. See `LICENSE` for more information.
