"""The file handler for the application."""
import asyncio
import tempfile
import zipfile
from logging import Logger
from pathlib import Path

import aiofiles

from app.settings import Settings


class FileHandler:
    """The file handler for the application."""

    def __init__(self, settings: Settings, logger: Logger) -> None:
        """Initialize the FileHandler.

        Args:
            settings: The settings object for the application.
            logger: The logger to use for the application.
        """
        self.settings = settings
        self.logger = logger

    def get_directory(self, dir_type: str = "file") -> Path:
        """Get the directory for the specified type.

        Args:
            dir_type: The type of the directory. Defaults to "file".

        Returns:
            The path of the directory.
        """
        return (
            Path(tempfile.gettempdir())
            if self.settings.use_sys_tmp
            else Path(getattr(self.settings, f"{dir_type}_directory"))
        )

    async def write_file(self, file_location: Path, file_content: bytes) -> None:
        """Write content to a file.

        Args:
            file_location: The location of the file.
            file_content: The content to write to the file.
        """
        try:
            # use aiofiles to write the file asynchronously
            async with aiofiles.open(file_location, "wb+") as file_object:
                self.logger.info("Writing file to %s", file_location)
                await file_object.write(file_content)
        except OSError:
            self.logger.exception("Error writing file")
            msg = f"Failed to write to file at {file_location}"
            raise RuntimeError(msg) from None

    async def create_zip(self, file_location: Path, zip_location: Path) -> None:
        """Create a zip file from a file.

        Args:
            file_location: The location of the file to zip.
            zip_location: The location of the zip file.
        """
        try:
            await asyncio.to_thread(self._create_zip, file_location, zip_location)
        except zipfile.BadZipFile:
            self.logger.exception("Error creating zip file")
            msg = f"Failed to create zip file at {zip_location}"
            raise RuntimeError(msg) from None

    def _create_zip(self, file_location: Path, zip_location: Path) -> None:
        """Synchronous helper function to create a zip file.

        This function is meant to be called inside an asyncio.to_thread to not block
        the event loop with synchronous I/O operations.

        Args:
            file_location: The location of the file to zip.
            zip_location: The location of the zip file.
        """
        with zipfile.ZipFile(zip_location, "w") as zip_ref:
            self.logger.info("Creating zip file at %s", zip_location)
            zip_ref.write(file_location, arcname=file_location.name)

    async def remove_file(self, file_location: Path) -> None:
        """Remove a file.

        Args:
            file_location: The location of the file to remove.
        """
        try:
            await asyncio.to_thread(file_location.unlink)
            self.logger.info("Deleted original file at %s", file_location)
        except OSError:
            self.logger.exception("Error deleting file")
            msg = f"Failed to delete file at {file_location}"
            raise RuntimeError(msg) from None
