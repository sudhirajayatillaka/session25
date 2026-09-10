import pytest
from playwright.sync_api import Page, expect


pytestmark = pytest.mark.level4


def test_hello_api_contract(api_client):
    response = api_client.get("/hello")
    assert response.status_code == 200, (
        "GET /hello should return status 200. Add the route in main.py."
    )
    assert response.json() == {"message": "Hello from FastAPI!"}, (
        'GET /hello should return exactly {"message": "Hello from FastAPI!"}.'
    )


def test_hello_button_displays_backend_message(page: Page, live_server: str):
    page.goto(live_server)
    page.locator("#hello-button").click()
    expect(page.locator("#hello-output")).to_have_text("Hello from FastAPI!")

