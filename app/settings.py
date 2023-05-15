"""Settings for the application that are loaded from environment variables."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings for the application that are loaded from environment variables."""

    file_directory: str
    zip_directory: str
    use_sys_tmp: bool = False

    class Config:  # noqa: D106
        env_file = ".env"
