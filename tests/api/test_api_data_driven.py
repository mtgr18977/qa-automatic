import os, csv, pytest, requests

API_BASE = os.getenv('API_BASE', 'https://httpbin.org')
CSV_PATH = os.path.join(os.path.dirname(__file__), 'data', 'sample_inputs.csv')

def load_inputs():
    rows = []
    with open(CSV_PATH, newline='') as f:
        reader = csv.DictReader(f, fieldnames=['q'])
        for r in reader:
            rows.append(r['q'])
    return rows

@pytest.mark.api
@pytest.mark.parametrize('q', load_inputs())
def test_api_search_param(q):
    url = f"{API_BASE}/get"
    r = requests.get(url, params={'q': q}, timeout=10)
    assert r.status_code == 200
    j = r.json()
    assert j.get('args', {}).get('q') == q
