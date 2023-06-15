"""Settings for the application that are loaded from environment variables."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings for the application that are loaded from environment variables."""

    file_directory: str = "files"
    zip_directory: str = "zipped_files"
    use_sys_tmp: bool = False
    max_file_size: int = 5242880
    cors_origin: str = "http://localhost:3000"
    port: int = 8000
    host: str = "localhost"

    class Config:  # noqa: D106
        env_file = ".env"
