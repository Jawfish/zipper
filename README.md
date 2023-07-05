# Zipper

Zipper is a webapp where users can upload files to receive a downloadable archive of them. The application is developed using the Python FastAPI framework.

## Getting Started

### Prerequisites

- Python 3.11
- [Poetry](https://python-poetry.org/) package manager

### Installation

1. Clone the repository

    ```bash
    git clone https://github.com/Jawfish/zipper.git
    cd zipper
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
MAX_FILE_SIZE=52428800
CORS_ORIGIN=http://localhost:5173
PORT=8000
HOST=localhost
VITE_MAX_FILE_SIZE=52428800
VITE_API_URL=http://localhost:8000
```

- `FILE_DIRECTORY`: The directory where uploaded files are temporarily stored while being zipped.
- `ZIP_DIRECTORY`: The directory where zipped files are temporarily stored while being downloaded by the user.
- `USE_SYS_TMP`: Whether or not to use the system's temporary directory for file storage.
- `MAX_FILE_SIZE`: The maximum file size that the backend will allow to be uploaded.
- `CORS_ORIGIN`: The URL of the frontend application.
- `PORT`: The port to run the backend application on.
- `HOST`: The host to run the backend application on.
- `VITE_MAX_FILE_SIZE`: The maximum file size that the frontend will allow to be uploaded.
- `VITE_API_URL`: The URL of the backend application as seen by the frontend.

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
