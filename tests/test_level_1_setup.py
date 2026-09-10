import pytest


pytestmark = pytest.mark.level1


def test_home_page_loads(api_client):
    response = api_client.get("/")
    assert response.status_code == 200, (
        "GET / should return the workshop HTML page with status 200."
    )
    assert "Web Development First Steps" in response.text, (
        "The workshop heading is missing from the HTML page. Restore static/index.html."
    )


@pytest.mark.parametrize("asset", ["styles.css", "script.js"])
def test_frontend_assets_load(api_client, asset):
    response = api_client.get(f"/static/{asset}")
    assert response.status_code == 200, (
        f"/static/{asset} did not load. Check app.mount() in main.py."
    )

