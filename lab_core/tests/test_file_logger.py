import pytest
from lab_core.context import FileLogger
import os
import tempfile


def test_filelogger_writes_and_closes_file():
    # Create a temporary file path
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        with FileLogger(path=tmp_path) as log_file:
            assert not log_file.closed
            log_file.write("Hello\n")

        # After context: file should be closed and content should be written
        with open(tmp_path, "r") as f:
            content = f.read()
            assert "Hello" in content

    finally:
        os.remove(tmp_path)
