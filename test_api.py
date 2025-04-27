import pytest
import requests

@pytest.fixture
def base_url():
    return "https://httpbin.org"

@pytest.mark.parametrize("endpoint, expected_status", [
    ("/status/200", 200),
    ("/get", 200),
])
def test_status_codes(base_url, endpoint, expected_status):
    resp = requests.get(f"{base_url}{endpoint}")
    assert resp.status_code == expected_status

def test_post_json(base_url):
    payload = {"name": "Bob", "age": 30}
    resp = requests.post(f"{base_url}/post", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["json"] == payload

@pytest.mark.parametrize("endpoint, expected_status", [
    ("/status/418", 418),
    ("/status/404", 404),
])
def test_error_codes(base_url, endpoint, expected_status):
    resp = requests.get(f"{base_url}{endpoint}")
    assert resp.status_code == expected_status

