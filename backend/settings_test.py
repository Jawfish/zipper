import os
from backend.settings import Settings


def test_settings_loaded_from_env():
    # Set environment variables
    os.environ["FILE_DIRECTORY"] = "/test/file/directory"
    os.environ["ZIP_DIRECTORY"] = "/test/zip/directory"
    os.environ["USE_SYS_TMP"] = "True"
    os.environ["MAX_FILE_SIZE"] = "5242880"
    os.environ["CORS_ORIGINS"] = "http://localhost:3000, https://example.com"
    os.environ["PORT"] = "8000"
    os.environ["HOST"] = "localhost"

    # Load settings
    settings = Settings()

    # Assert that settings match the environment variables
    assert settings.file_directory == "/test/file/directory"
    assert settings.zip_directory == "/test/zip/directory"
    assert settings.use_sys_tmp is True
    assert settings.max_file_size == 5242880
