from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="Web Development First Steps")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", include_in_schema=False)
def read_home() -> FileResponse:
    """Serve the workshop page."""
    return FileResponse(STATIC_DIR / "index.html")


# TODO Level 4: Add GET /hello.
# It should return: {"message": "Hello from FastAPI!"}


# TODO Level 5:
# 1. Create a Pydantic model with username and password fields.
# 2. Add POST /login.
# 3. Accept student / webdev123 and reject other credentials.
