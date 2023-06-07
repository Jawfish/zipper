import pytest
from unittest.mock import MagicMock, patch

from fastapi import APIRouter
from backend.app_factory import create_app, AppState
from backend.file_handler import FileHandler
from logging import Logger
from backend.settings import Settings


def test_app_state_initialization():
    mock_file_handler = MagicMock(spec=FileHandler)
    mock_logger = MagicMock(spec=Logger)
    mock_settings = MagicMock(spec=Settings)

    app_state = AppState(
        file_handler=mock_file_handler, logger=mock_logger, settings=mock_settings
    )

    assert app_state.file_handler is mock_file_handler
    assert app_state.logger is mock_logger


def test_create_app():
    mock_file_handler = MagicMock(spec=FileHandler)
    mock_logger = MagicMock(spec=Logger)
    mock_routers = [APIRouter(), APIRouter()]
    mock_settings = MagicMock(spec=Settings)

    initial_route_count = len(mock_routers)

    app = create_app(
        file_handler=mock_file_handler,
        routers=mock_routers,
        logger=mock_logger,
        settings=mock_settings,
    )

    # Asserts that the app state is an instance of AppState
    assert isinstance(app.state, AppState)

    # Asserts that the app state was created with the correct parameters
    assert app.state.file_handler is mock_file_handler
    assert app.state.logger is mock_logger
    assert app.state.settings is mock_settings

    # Asserts that the logger was called with the correct message
    mock_logger.info.assert_called_once_with("Application created")

    # Asserts that each router was included in the app
    assert len(app.routes) >= initial_route_count
