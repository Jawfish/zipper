# Zipper

Zipper is a webapp where users can upload files to receive a downloadable archive of them. The application is developed using the Python FastAPI framework.

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
    poetry run backend
    ```

## Configuration

Application settings are loaded from environment variables which are set in a `.env` file. An example `.env` file would look like this:

```ini
FILE_DIRECTORY=./files
ZIP_DIRECTORY=./zipped_files
USE_SYS_TMP=true
MAX_FILE_SIZE=5242880 # 5MB
```

- `FILE_DIRECTORY`: The directory where uploaded files are temporarily stored.
- `ZIP_DIRECTORY`: The directory where zipped files are stored.
- `USE_SYS_TMP`: Whether or not to use the system's temporary directory for file storage.
- `MAX_FILE_SIZE`: The maximum allowed file size for uploads in bytes.

## Contributing

### TL;DR

```bash
# create a new branch
git checkout -b my-feature

# install dependencies
poetry install

# run app
poetry run backend

# run checks
poetry run nox

# stage changes
git add .

# commit with conventional commit style
git commit -m "tag: short description"
```

## License

Distributed under the MIT License. See `LICENSE` for more information.
