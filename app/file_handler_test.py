import asyncio
import zipfile
import pytest
from unittest.mock import Mock
from pathlib import Path
from tempfile import TemporaryDirectory
from app.file_handler import FileHandler


class MockSettings:
    use_sys_tmp = False
    file_directory = "/tmp"
    zip_directory = "/tmp"


class MockLogger:
    def info(self, *args, **kwargs):
        pass

    def exception(self, *args, **kwargs):
        pass


@pytest.fixture
def file_handler():
    settings = MockSettings()
    logger = MockLogger()
    return FileHandler(settings, logger)


@pytest.mark.asyncio
async def test_write_file(file_handler):
    with TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "test.txt"
        await file_handler.write_file(file_path, b"test content")
        assert file_path.exists()


@pytest.mark.asyncio
async def test_create_zip(file_handler):
    with TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "test.txt"
        zip_path = Path(tmpdir) / "test.zip"
        await file_handler.write_file(file_path, b"test content")
        await file_handler.create_zip(file_path, zip_path)
        assert zip_path.exists()

        # Check that the zip file contains the expected file
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            assert "test.txt" in zip_ref.namelist()


@pytest.mark.asyncio
async def test_remove_file(file_handler):
    with TemporaryDirectory() as tmpdir:
        file_path = Path(tmpdir) / "test.txt"
        await file_handler.write_file(file_path, b"test content")
        assert file_path.exists()
        await file_handler.remove_file(file_path)
        assert not file_path.exists()


def test_get_directory(file_handler):
    assert file_handler.get_directory() == Path("/tmp")
