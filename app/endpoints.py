"""Endpoints for the API."""
from logging import Logger
from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from fastapi.responses import FileResponse

from app.dependencies import get_file_handler, get_logger
from app.file_handler import FileHandler

if TYPE_CHECKING:
    from pathlib import Path


router = APIRouter()


@router.post("/zip", response_model=None)
async def zip_file(
    file: UploadFile | None = None,
    file_handler: FileHandler = Depends(get_file_handler),
    logger: Logger = Depends(get_logger),
) -> FileResponse:
    """Zip a file and return it.

    Args:
        file: The file to zip. Defaults to None.
        file_handler: The file handler to use.
        logger: The logger to use.

    Raises:
        HTTPException: If the file is not found.

    Returns:
        FileResponse: The zipped file.
    """
    if file and file.filename is not None:
        logger.info("Received file %s", file.filename)
        file_dir = file_handler.get_directory("file")
        zip_dir = file_handler.get_directory("zip")

        file_dir.mkdir(parents=True, exist_ok=True)
        zip_dir.mkdir(parents=True, exist_ok=True)

        file_path: Path = file_dir / file.filename
        await file_handler.write_file(file_path, await file.read())

        zip_location = zip_dir / f"{file.filename}.zip"
        await file_handler.create_zip(file_path, zip_location)

        await file_handler.remove_file(file_path)

        response_file = FileResponse(
            str(zip_location),
            media_type="application/zip",
            filename=f"{file.filename}.zip",
        )

        logger.info("Returning file %s", response_file.filename)

        return response_file

    raise HTTPException(status_code=400, detail="File not found")
