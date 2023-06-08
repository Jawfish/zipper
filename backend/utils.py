"""Utility functions for the backend."""


def sanitize_filename(filename: str) -> str:
    """Sanitize a filename to prevent directory traversal.

    Args:
        filename: The filename to sanitize.

    Returns:
        str: The sanitized filename.
    """
    from werkzeug.utils import secure_filename

    return secure_filename(filename)
