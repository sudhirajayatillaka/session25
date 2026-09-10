import re

import pytest
from playwright.sync_api import Page, expect


pytestmark = pytest.mark.level3


def test_login_fields_are_marked_required(page: Page, live_server: str):
    page.goto(live_server)
    assert page.locator("#username").get_attribute("required") is not None, (
        "Add the required attribute to #username."
    )
    assert page.locator("#password").get_attribute("required") is not None, (
        "Add the required attribute to #password."
    )


def test_blank_login_shows_error_without_request(page: Page, live_server: str):
    login_requests: list[str] = []

    def observe_request(request):
        if request.url.endswith("/login"):
            login_requests.append(request.url)

    page.on("request", observe_request)
    page.goto(live_server)
    page.locator("#login-form button[type='submit']").click()

    message = page.locator("#login-message")
    expect(message).to_have_class(re.compile(r"(^|\s)error(\s|$)"))
    expect(message).not_to_be_empty()
    assert not login_requests, (
        "Blank fields should be stopped in JavaScript before POST /login is called."
    )


def test_completed_form_shows_success_state(page: Page, live_server: str):
    page.route(
        "**/login",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body='{"success":true,"message":"Login successful"}',
        ),
    )
    page.goto(live_server)
    page.locator("#username").fill("student")
    page.locator("#password").fill("webdev123")
    page.locator("#login-form button[type='submit']").click()

    message = page.locator("#login-message")
    expect(message).to_have_class(re.compile(r"(^|\s)success(\s|$)"))
    expect(message).not_to_be_empty()
