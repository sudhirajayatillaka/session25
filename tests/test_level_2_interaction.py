import pytest
from playwright.sync_api import Page


pytestmark = pytest.mark.level2


def test_name_button_displays_the_input(page: Page, live_server: str):
    page.goto(live_server)
    page.locator("#name-input").fill("Ada")
    page.locator("#show-name-button").click()

    output = page.locator("#name-output")
    output.wait_for(state="visible")
    assert "Ada" in output.inner_text(), (
        "After clicking Show greeting, #name-output should contain the value from "
        "#name-input. Check your querySelector calls and click event listener."
    )

