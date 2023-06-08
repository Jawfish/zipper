import pytest
from backend.utils import sanitize_filename


def test_sanitize_filename():
    normal_filename = "testfile.txt"
    sanitized = sanitize_filename(normal_filename)
    assert (
        sanitized == normal_filename
    ), "Sanitized filename is not as expected for normal filename."

    filename_with_slashes = "../testfile.txt"
    sanitized = sanitize_filename(filename_with_slashes)
    assert (
        sanitized == "testfile.txt"
    ), "Sanitized filename is not as expected for filename with slashes."

    filename_with_special_chars = "test*file?.txt"
    sanitized = sanitize_filename(filename_with_special_chars)
    assert (
        sanitized == "testfile.txt"
    ), "Sanitized filename is not as expected for filename with special characters."

    filename_with_non_ascii_chars = "tęstfile.txt"
    sanitized = sanitize_filename(filename_with_non_ascii_chars)
    assert (
        sanitized == "testfile.txt"
    ), "Sanitized filename is not as expected for filename with non-ASCII characters."


@pytest.mark.parametrize(
    "filename,expected",
    [
        ("normal_filename.txt", "normal_filename.txt"),
        ("../unsafe_filename.txt", "unsafe_filename.txt"),
        ("test*file?.txt", "testfile.txt"),
        ("tęstfile.txt", "testfile.txt"),
    ],
)
def test_sanitize_filename_parametrized(filename, expected):
    result = sanitize_filename(filename)
    assert result == expected, f"For {filename}, expected {expected} but got {result}."
