"""Entrypoint for the application."""
import uvicorn

from app.app_factory import create_app
from app.endpoints import router
from app.file_handler import FileHandler
from app.logger import set_up_logger
from app.settings import Settings


def main() -> None:
    """Entrypoint for the application."""
    settings = Settings()

    logger = set_up_logger()

    file_handler = FileHandler(settings, logger)
    server = create_app(file_handler, [router], logger)
    uvicorn.run(server, host="localhost", port=8000)


if __name__ == "__main__":
    main()
