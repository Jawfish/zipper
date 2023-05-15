import pytest
from fastapi.testclient import TestClient
from fastapi import UploadFile
from io import BytesIO

from app.app_factory import create_app
from app.file_handler import FileHandler
from app.endpoints import router
from app.logger import set_up_logger
from app.settings import Settings

settings = Settings()
logger = set_up_logger()
client = TestClient(create_app(FileHandler(settings, logger), [router], logger))


def create_upload_file(filename: str, content: str) -> UploadFile:
    return UploadFile(filename=filename, file=BytesIO(content.encode()))


@pytest.mark.asyncio
async def test_zip_file():
    upload_file = create_upload_file("test.txt", "test content")

    response = client.post(
        "/zip",
        files={
            "file": (upload_file.filename, upload_file.file, upload_file.content_type)
        },
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/zip"


@pytest.mark.asyncio
async def test_zip_file_no_file():
    response = client.post("/zip")
    assert response.status_code == 400
    assert response.json() == {"detail": "File not found"}
