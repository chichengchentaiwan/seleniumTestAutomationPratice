# QA Automation assignment

## Prerequisite

* Install selenium(https://pypi.org/project/selenium/)
  * `pip install -U selenium`
* Make sure you have correct webdrivers you need in your local
  * For installation, please check https://pypi.org/project/selenium/
* Install pytest(https://docs.pytest.org/en/7.2.x/getting-started.html)
  * `pip install -U pytest`

## How to run the test

* If you want to execute all the tests
  * In your terminal, under this project, call `pytest`
* If you want to execute single test case
  * In your terminal, under this project, call `pytest -k ${TheTestCaseName}`
  * Ex: `pytest -k test_login_with_blank_password`