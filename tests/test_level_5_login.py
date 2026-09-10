import re

import pytest
from playwright.sync_api import Page, expect


pytestmark = pytest.mark.level5


def test_valid_login_api_contract(api_client):
    response = api_client.post(
        "/login", json={"username": "student", "password": "webdev123"}
    )
    assert response.status_code == 200, (
        "POST /login should return status 200 for student / webdev123."
    )
    assert response.json() == {"success": True, "message": "Login successful"}, (
        "The successful login JSON does not match the workshop contract."
    )


def test_invalid_login_api_contract(api_client):
    response = api_client.post(
        "/login", json={"username": "student", "password": "wrong"}
    )
    assert response.status_code == 401, (
        "POST /login should return status 401 for incorrect credentials."
    )
    assert response.json() == {"detail": "Invalid username or password"}, (
        "The invalid-login message does not match the workshop contract."
    )


def test_login_requires_both_json_fields(api_client):
    response = api_client.post("/login", json={"username": "student"})
    assert response.status_code == 422, (
        "Use a Pydantic request model so FastAPI returns 422 when password is missing."
    )


def test_browser_sends_json_and_displays_success(page: Page, live_server: str):
    captured: dict[str, object] = {}

    def capture_login(route, request):
        captured["content_type"] = request.headers.get("content-type", "")
        captured["body"] = request.post_data_json
        route.continue_()

    page.route("**/login", capture_login)
    page.goto(live_server)
    page.locator("#username").fill("student")
    page.locator("#password").fill("webdev123")
    page.locator("#login-form button[type='submit']").click()

    expect(page.locator("#login-message")).to_have_class(
        re.compile(r"(^|\s)success(\s|$)")
    )
    expect(page.locator("#login-message")).to_contain_text("Login successful")
    assert "application/json" in str(captured.get("content_type", "")), (
        "POST /login must include Content-Type: application/json."
    )
    assert captured.get("body") == {
        "username": "student",
        "password": "webdev123",
    }, "Use JSON.stringify({ username, password }) as the fetch body."


def test_browser_displays_invalid_login(page: Page, live_server: str):
    page.goto(live_server)
    page.locator("#username").fill("student")
    page.locator("#password").fill("wrong")
    page.locator("#login-form button[type='submit']").click()

    expect(page.locator("#login-message")).to_have_class(
        re.compile(r"(^|\s)error(\s|$)")
    )
    expect(page.locator("#login-message")).to_contain_text(
        "Invalid username or password"
    )
