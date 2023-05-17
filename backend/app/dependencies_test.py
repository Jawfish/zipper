import pytest
from unittest.mock import MagicMock, patch

from fastapi import Request
from app.dependencies import get_file_handler, get_logger
from app.file_handler import FileHandler
from app.app_factory import AppState
from logging import Logger


def test_get_logger():
    mock_request = MagicMock(spec=Request)
    mock_logger = MagicMock(spec=Logger)
    mock_state = AppState(file_handler=MagicMock(spec=FileHandler), logger=mock_logger)

    mock_request.app.state = mock_state

    logger = get_logger(mock_request)
    assert logger is mock_logger


def test_get_file_handler():
    mock_request = MagicMock(spec=Request)
    mock_file_handler = MagicMock(spec=FileHandler)
    mock_state = AppState(file_handler=mock_file_handler, logger=MagicMock(spec=Logger))

    mock_request.app.state = mock_state

    file_handler = get_file_handler(mock_request)
    assert file_handler is mock_file_handler
