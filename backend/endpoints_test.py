from dotenv import load_dotenv
import pytest
from fastapi.testclient import TestClient
from fastapi import UploadFile
from io import BytesIO

from backend.app_factory import create_app
from backend.file_handler import FileHandler
from backend.endpoints import router
from backend.logger import set_up_logger
from backend.settings import Settings

load_dotenv()
settings = Settings()
logger = set_up_logger()
client = TestClient(create_app(FileHandler(settings, logger), [router], logger))


def create_upload_file(filename: str, content: str) -> UploadFile:
    return UploadFile(filename=filename, file=BytesIO(content.encode()))


@pytest.mark.asyncio
async def test_zip_files():
    upload_file1 = create_upload_file("test1.txt", "test content 1")
    upload_file2 = create_upload_file("test2.txt", "test content 2")

    response = client.post(
        "/zip",
        files=[
            ("files", (upload_file1.filename, upload_file1.file, "text/plain")),
            ("files", (upload_file2.filename, upload_file2.file, "text/plain")),
        ],
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/zip"
