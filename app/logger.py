"""Logger module for the application."""
import logging
from logging import StreamHandler


def set_up_logger() -> logging.Logger:
    """Set up the logger for the application.

    Returns:
        The logger for the application.
    """
    log_format = "%(levelname)s:     %(message)s"
    formatter = logging.Formatter(log_format)

    logger = logging.getLogger(__name__)

    handler = StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger
