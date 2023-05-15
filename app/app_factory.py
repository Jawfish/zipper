"""This module provides the factory function for creating the FastAPI application.

The FastAPI application is created with an application state object, AppState, which
holds references to the file handler and the logger, enabling their usage across
different parts of the application. The factory function takes routers to include in
the application, which ensures that the application state is available to the endpoints,
regardless of the router they are defined in.
"""
from logging import Logger

from fastapi import APIRouter, FastAPI
from starlette.datastructures import State

from app.file_handler import FileHandler


class AppState(State):
    """The application state object for the FastAPI application.

    AppState inherits from the starlette.datastructures.State class, which provides a
    mapping for storing arbitrary attributes. AppState is used to inject the file
    handler and logger into the application. These can be accessed by the endpoints via
    the app state (app.state.file_handler and app.state.logger), regardless of which
    router the endpoint is defined in.

    Attributes:
        file_handler (FileHandler): The file handler to use for the application.
        logger (Logger): The logger to use for the application.
    """

    def __init__(self, file_handler: FileHandler, logger: Logger) -> None:
        """Initializes a new instance of AppState.

        AppState is used to inject the database and logger into the application so that
        they can be accessed by the endpoints via the app state (app.state.database and
        app.state.logger), regardless of which router the endpoint is defined in.5


        Args:
            file_handler: The file handler to use for the application.
            logger: The logger to use for the application.
        """
        super().__init__()
        self.file_handler = file_handler
        self.logger = logger


class App(FastAPI):
    """The FastAPI application.

    App inherits from the FastAPI class and is the main entry point for the FastAPI
    application. It holds an instance of AppState as its state, allowing the file
    handler and logger to be accessed throughout the application.

    Attributes:
        state (AppState): The application state for the application.
    """

    def __init__(self, state: AppState) -> None:
        """Initializes a new App instance with the given state.

        Args:
            state: The application state to use for the application.
        """
        super().__init__()
        self.state = state


def create_app(
    file_handler: FileHandler,
    routers: list[APIRouter],
    logger: Logger,
) -> App:
    """Factory function for creating the FastAPI application.

    Args:
        file_handler: The file handler to use for the application.
        routers: The routers to include in the application.
        logger: The logger to use for the application.

    Returns:
        The FastAPI application.
    """
    state = AppState(file_handler, logger)
    app = App(state=state)

    state.logger.info("Application created")

    # Include the routers in the application. This is done to ensure that the
    # application state is available to all endpoints, regardless of which router
    # they are defined in.
    for router in routers:
        app.include_router(router)

    return app
