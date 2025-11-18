import os
import requests
import pytest

API_BASE = os.getenv('API_BASE', 'https://httpbin.org')
AUTH_TOKEN = os.getenv('AUTH_TOKEN', '')

@pytest.mark.api
def test_api_auth_bearer():
    headers = {}
    if AUTH_TOKEN:
        headers['Authorization'] = f'Bearer {AUTH_TOKEN}'
    r = requests.get(f"{API_BASE}/bearer", headers=headers, timeout=10)
    assert r.status_code in (200, 401)
