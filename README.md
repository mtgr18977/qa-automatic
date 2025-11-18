# QA Automation - Playwright (Python) + pytest (API)

Ready-to-use starter repository for UI and API automation with Python.

## Features
- Playwright (Python) for UI tests
- pytest + requests for API tests
- GitHub Actions workflow for CI
- Docker support for reproducible runs
- Examples: auth, data-driven, visual-diff

## Quick start
1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Playwright browsers:
   ```bash
   playwright install
   ```
4. Run tests:
   ```bash
   pytest -q
   ```
