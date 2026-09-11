from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel


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
@app.get("/hello")
async def root():
    return {"message": "Hello from FastAPI!"}


# TODO Level 5:
# 1. Create a Pydantic model with username and password fields.
# 2. Add POST /login.
# 3. Accept student / webdev123 and reject other credentials.

class Item(BaseModel):
    username: str
    password: str

class ItemResponse(BaseModel):
    username: str
    password: str

@app.post("/login")
async def create_item(item: Item):
    if (item.username == "student") and (item.password == "webdev123"):
        pass
    else:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )
    return {"success": True, "message": "Login successful"}
