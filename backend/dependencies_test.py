import pytest
from unittest.mock import MagicMock, patch

from fastapi import Request
from backend.dependencies import get_file_handler, get_logger, get_settings
from backend.file_handler import FileHandler
from backend.app_factory import AppState
from logging import Logger
from backend.settings import Settings


def test_get_logger():
    mock_request = MagicMock(spec=Request)
    mock_logger = MagicMock(spec=Logger)
    mock_state = AppState(
        file_handler=MagicMock(spec=FileHandler),
        logger=mock_logger,
        settings=MagicMock(spec=Settings),
    )

    mock_request.app.state = mock_state

    logger = get_logger(mock_request)
    assert logger is mock_logger


def test_get_file_handler():
    mock_request = MagicMock(spec=Request)
    mock_file_handler = MagicMock(spec=FileHandler)
    mock_state = AppState(
        file_handler=mock_file_handler,
        logger=MagicMock(spec=Logger),
        settings=MagicMock(spec=Settings),
    )

    mock_request.app.state = mock_state

    file_handler = get_file_handler(mock_request)
    assert file_handler is mock_file_handler


def test_get_settings():
    mock_request = MagicMock(spec=Request)
    mock_settings = MagicMock(spec=Settings)
    mock_state = AppState(
        file_handler=MagicMock(spec=FileHandler),
        logger=MagicMock(spec=Logger),
        settings=mock_settings,
    )

    mock_request.app.state = mock_state

    settings = get_settings(mock_request)
    assert settings is mock_settings
