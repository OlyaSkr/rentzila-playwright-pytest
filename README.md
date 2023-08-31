# Description

This is [Python] Playwright - Pytest project with allure report

### Setup:

1. Clone repo using git clone https://github.com/OlyaSkr/rentzila-playwright-pytest.git
2. Install Python 3.11+
3. Install package manager: pip install pipenv
4. Create an isolated virtual environment: pipenv shell

### Installing libraries and dependencies:

1. pipenv install pytest-playwright
2. playwright install chromium
3. pipenv install allure-pytest

### Run all playwright tests:
pytest

### Run allure report:

allure serve reports