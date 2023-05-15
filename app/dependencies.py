"""Provides dependencies for endpoints.

Dependencies are functions that are used to inject objects into endpoints. This is
useful for providing access to objects that are used by multiple endpoints, like the
logger and file handler.


Applications are created with the application factory. Each application instance has
its own state object, so when the endpoints are defined for that application, it passes
that state object to those endpoints. The state for a given application is then
accessible through the request object: request.app.state.
"""

from logging import Logger
from typing import TYPE_CHECKING

from fastapi import Request

from app.file_handler import FileHandler

if TYPE_CHECKING:
    from app.app_factory import AppState


def get_logger(request: Request) -> Logger:
    """Provides endpoints access to the given application's logger.

    Args:
        request: The request object for the endpoint.

    Returns:
        The logger for the application.
    Usage:
        @router.get("/test")
        async def test(logger: Logger = Depends(get_logger)) -> dict:
            logger.info("Hello world")
            return {"message": "hello world"}
    """
    app_state: AppState = request.app.state
    return app_state.logger


def get_file_handler(request: Request) -> FileHandler:
    """Provides endpoints access to the given application's file handler.

    Args:
        request: The request object for the endpoint.

    Returns:
        The file handler for the application.
    Usage:
        @router.get("/test")
        async def test(file_handler: FileHandler = Depends(get_file_handler)) -> dict:
            file_handler.write_file("test.txt", "Hello world")
            return FileResponse("test.txt")
    """
    app_state: AppState = request.app.state
    return app_state.file_handler
