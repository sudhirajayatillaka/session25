from __future__ import annotations

import os
from pathlib import Path
import socket
import subprocess
import sys
import time
from urllib.error import URLError
from urllib.request import urlopen

import pytest
import httpx


@pytest.fixture(scope="session")
def project_root() -> Path:
    return Path(os.environ["WEBDEV_PROJECT_ROOT"]).resolve()


def unused_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


@pytest.fixture(scope="session")
def live_server(project_root: Path) -> str:
    port = unused_port()
    url = f"http://127.0.0.1:{port}"
    env = os.environ.copy()
    env["PYTHONPATH"] = str(project_root)
    process = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "main:app",
            "--host",
            "127.0.0.1",
            "--port",
            str(port),
        ],
        cwd=project_root,
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    deadline = time.monotonic() + 10
    while time.monotonic() < deadline:
        if process.poll() is not None:
            pytest.fail(
                "FastAPI stopped while starting. Run start.bat and fix the first error shown."
            )
        try:
            with urlopen(url, timeout=0.5) as response:
                if response.status == 200:
                    break
        except (URLError, TimeoutError):
            time.sleep(0.1)
    else:
        process.terminate()
        pytest.fail("FastAPI did not start within 10 seconds. Try running start.bat.")

    yield url

    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()


@pytest.fixture()
def api_client(live_server: str):
    with httpx.Client(base_url=live_server, timeout=5) as client:
        yield client
