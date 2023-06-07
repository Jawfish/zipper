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
settings = Settings(max_file_size=100)  # use low value so that test files will be small
logger = set_up_logger()
client = TestClient(
    create_app(FileHandler(settings, logger), [router], logger, settings)
)


def create_upload_file(filename: str, content: str) -> UploadFile:
    return UploadFile(filename=filename, file=BytesIO(content.encode()))


@pytest.fixture
def mock_settings():
    """Returns a mock Settings instance with a small max_file_size value."""
    return Settings(max_file_size=10)


@pytest.mark.asyncio
async def test_zip_files():
    upload_file1 = create_upload_file("test1.txt", "a" * (settings.max_file_size // 2))
    upload_file2 = create_upload_file("test2.txt", "b" * (settings.max_file_size // 2))

    response = client.post(
        "/zip",
        files=[
            ("files", (upload_file1.filename, upload_file1.file, "text/plain")),
            ("files", (upload_file2.filename, upload_file2.file, "text/plain")),
        ],
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/zip"


@pytest.mark.asyncio
async def test_zip_files_size_limit():
    small_upload_file = create_upload_file("small.txt", "small content")
    large_content = "a" * (settings.max_file_size + 1)
    large_upload_file = create_upload_file("large.txt", large_content)

    response = client.post(
        "/zip",
        files=[
            (
                "files",
                (small_upload_file.filename, small_upload_file.file, "text/plain"),
            ),
            (
                "files",
                (large_upload_file.filename, large_upload_file.file, "text/plain"),
            ),
        ],
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Total file size too large"}
