## Code Structure

```
root
├── twikkie_autotest/
│   ├── base/
|   |   ├── __init__.py
│   │   ├── base_api.py
│   │   ├── base_page.py
│   │   ├── selenium_driver.py
|   ├── drivers/
|   ├── pages/
|   |   ├── login_page
|   |   |   ├── __init__.py
|   |   |   ├── login_page.py
|   |   ├── signup_page 
|   |   |   ├── __init__.py
|   |   |   ├── signup_page.py
|   ├── tests/
|   |   ├── test_login_page
|   |   |   ├── test_login_page.py
|   |   ├── test_signup_page
|   |   |   ├── test_signup_page.py
|   ├── utilities/
|   |   ├── custom_logger.py
|   |   ├── test_status.py
|   |   ├── util.py
├── .gitignore
├── prepare_enviroment.bat
├── pytest.ini
├── README.md
└── runPytest.bat
```

- `twikkie_autotest/`: This directory contains the  test files
    - `base/`:
        - `__init__.py/`:  Initializes the base module.
        - `base_api.py/`:   Contains base functionalities for API interactions, providing common methods and utilities for making API requests.
        - `base_page.py/`:  Provides a base class for all page objects, including common methods for interacting with web elements and handling page-specific actions.
        - `selenium_driver.py/`: Manages the Selenium WebDriver setup and configuration, including browser initialization and teardown procedures.
    - `drivers/`:
    - `pages/`: Contains login and signup files
        - `login_page`/:
            - `_init__.py`/: Initializes the base module.
            - `login_page.py`/: Contains locators, test data and functions for login page
        - `signup_page `/: 
            - `__init__.py`/: Initializes the base module.
            - `signup_page.py`/: Contains locators, test data and functions for signup page
    - `tests/`:
        - `test_login_page`/:
            - `test_login_page.py`/: Contains test cases on login functionality
        - `test_signup_page`/: 
            - `test_signup_page.py`/: Contains test cases on signup functionality
    - `utilities/`:
        - `custom_logger.py`/: Custom logging utility for creating detailed test execution logs.
        - `test_status.py`/: Utility for tracking and reporting the status of test cases.
        - `util.py`/: Contains various utility functions used across the project.
- `.gitignore/`: Contains files and directories that should not be committed 
- `prepare_enviroment.bat`: Batch script for setting up the test environment.
- `pytest.ini`: Configuration file for pytest.
- `README.md`: This file, providing an overview of the project.
- `runPytest.bat`: Batch script to run pytest.


## Getting Started

### Prerequisites

- Python 3.8 or higher
- Selenium WebDriver
- pytest

### Installation

1. Clone the repository:
   ```sh
  https://github.com/vardanyangag/twikkie_autotest
2. Navigate to the project directory:
   ```sh
   cd twikkie_autotest
3. Install the required Python packages:
    ```sh
   pip install -r requirements.txt

### Running Tests

1. Prepare the environment by running:
   ```sh
   prepare_environment.bat
2. Execute tests using pytest:
   ```sh
   runPytest.bat
