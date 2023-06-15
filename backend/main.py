"""Entrypoint for the application."""
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from backend.app_factory import create_app
from backend.endpoints import router
from backend.file_handler import FileHandler
from backend.logger import set_up_logger
from backend.settings import Settings


def main() -> None:
    """Entrypoint for the application."""
    settings = Settings()

    logger = set_up_logger()

    file_handler = FileHandler(settings, logger)
    server = create_app(file_handler, [router], logger, settings)
    server.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.cors_origin],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    uvicorn.run(server, host=settings.host, port=settings.port)


if __name__ == "__main__":
    main()
