"""
Configuration file for Selenium tests
"""

# Browser configuration
BROWSER = 'chrome'

# Timeouts (in seconds)
TIMEOUTS = {
    'implicit': 10,      # Wait for elements to appear
    'page_load': 30,     # Wait for page to load
    'script': 30         # Wait for scripts to execute
}

# Base URLs for different environments
URLS = {
    'local': 'http://localhost:3000',
    'dev': 'https://dev.operationhope.com',
    'qa': 'https://qa.operationhope.com',
    'prod': 'https://www.operationhope.com'
}

# Screenshot configuration
SCREENSHOTS = {
    'enabled': True,
    'path': './screenshots',
    'on_failure': True
}

# Chrome options
CHROME_OPTIONS = {
    'args': [
        # '--headless',  # Uncomment to run in headless mode
        '--no-sandbox',
        '--disable-dev-shm-usage',
        '--window-size=1920,1080',
        '--disable-gpu'
    ]
}
