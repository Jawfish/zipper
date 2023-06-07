"""Endpoints for the API."""
from logging import Logger
from zipfile import ZipFile

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from fastapi.responses import FileResponse

from backend.dependencies import get_file_handler, get_logger, get_settings
from backend.file_handler import FileHandler
from backend.settings import Settings

router = APIRouter()


@router.post("/zip", response_model=None)
async def zip_files(
    file_handler: FileHandler = Depends(get_file_handler),
    logger: Logger = Depends(get_logger),
    settings: Settings = Depends(get_settings),
    files: list[UploadFile] | None = None,
) -> FileResponse:
    """Zip multiple files and return them.

    Args:
        files: The files to zip. Defaults to None.
        file_handler: The file handler to use.
        logger: The logger to use.
        settings: The settings to use.

    Raises:
        HTTPException: If any of the files are not found.

    Returns:
        FileResponse: The zipped files.
    """
    files = files or []
    total_size = 0

    logger.info("Received %d files", len(files))

    zip_dir = file_handler.get_directory(settings.zip_directory)

    zip_dir.mkdir(parents=True, exist_ok=True)

    zip_location = zip_dir / "files.zip"  # TODO: UUID for filename

    with ZipFile(zip_location, "w") as zip_file:
        for file in files:
            if file.filename is not None:
                content = await file.read()
                total_size += len(content)

                if total_size > settings.max_file_size:
                    raise HTTPException(
                        status_code=400,
                        detail="Total file size too large",
                    )

                logger.info("Received file %s", file.filename)
                zip_file.writestr(file.filename, content)

    if not zip_file.namelist():
        raise HTTPException(status_code=400, detail="No files found")

    response_file = FileResponse(
        str(zip_location),
        media_type="application/zip",
        filename="files.zip",  # TODO: don't hardcode filename
    )

    logger.info("Returning file %s", response_file.filename)

    return response_file
