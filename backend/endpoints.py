"""Endpoints for the API."""
from logging import Logger
from zipfile import ZipFile

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from fastapi.responses import FileResponse

from backend.dependencies import get_file_handler, get_logger
from backend.file_handler import FileHandler

router = APIRouter()


@router.post("/zip", response_model=None)
async def zip_files(
    file_handler: FileHandler = Depends(get_file_handler),
    logger: Logger = Depends(get_logger),
    files: list[UploadFile] | None = None,
) -> FileResponse:
    """Zip multiple files and return them.

    Args:
        files: The files to zip. Defaults to None.
        file_handler: The file handler to use.
        logger: The logger to use.

    Raises:
        HTTPException: If any of the files are not found.

    Returns:
        FileResponse: The zipped files.
    """
    files = files or []

    logger.info("Received %d files", len(files))

    file_handler.get_directory("file")
    zip_dir = file_handler.get_directory("zip")

    zip_dir.mkdir(parents=True, exist_ok=True)

    zip_location = zip_dir / "files.zip"

    with ZipFile(zip_location, "w") as zip_file:
        for file in files:
            if file.filename is not None:
                logger.info("Received file %s", file.filename)

                zip_file.writestr(file.filename, await file.read())

    if not zip_file.namelist():
        raise HTTPException(status_code=400, detail="No files found")

    response_file = FileResponse(
        str(zip_location),
        media_type="application/zip",
        filename="files.zip",
    )

    logger.info("Returning file %s", response_file.filename)

    return response_file
