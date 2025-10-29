# Selenium Tests for Operation Hope (Python)

This folder contains Selenium automated tests for the Operation Hope project, written in Python.

## Setup

### Prerequisites

- Python 3.8 or higher installed
- Chrome browser installed

### Installation

1. Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

### Run a single test

```bash
python tests/example_test.py
```

### Run the support ticket test

```bash
python tests/support_ticket_test.py
```

### Run all tests

```bash
python -m pytest tests/
```

## Project Structure

```
selenium-tests-py/
├── tests/              # Test files go here
│   ├── example_test.py
│   └── support_ticket_test.py
├── config/             # Configuration files
│   └── config.py
├── utils/              # Helper functions
│   └── helpers.py
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Writing Tests

Each test file should:

1. Import selenium webdriver
2. Create a driver instance
3. Perform test actions
4. Close the driver when done

Example:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def example_test():
    driver = webdriver.Chrome()
    try:
        driver.get('http://www.example.com')
        # Your test logic here
    finally:
        driver.quit()

if __name__ == '__main__':
    example_test()
```

## Notes

- Make sure Chrome browser is installed
- ChromeDriver is automatically managed by webdriver-manager
- Tests run in Chrome by default
- Each test file is independent
