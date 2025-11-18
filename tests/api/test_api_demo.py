import os
import requests
import pytest

API_BASE = os.getenv('API_BASE', 'https://httpbin.org')

@pytest.mark.api
def test_api_status_httpbin():
    r = requests.get(f"{API_BASE}/status/200", timeout=10)
    assert r.status_code == 200

@pytest.mark.api
def test_api_get_json_httpbin():
    r = requests.get(f"{API_BASE}/get", params={'q': 'test'}, timeout=10)
    assert r.status_code == 200
    body = r.json()
    assert 'args' in body
    assert body['args'].get('q') == 'test'
