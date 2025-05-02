# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests against"
    )

@pytest.fixture(scope="module")
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        opts = ChromeOptions()
        opts.add_argument("--headless=new")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--window-size=1920,1080")

        # disable password prompts
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        opts.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=opts)

    else:  # firefox
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        opts.add_argument("--width=1920")
        opts.add_argument("--height=1080")
        
        # disable password prompts in Firefox
        opts.set_preference("signon.rememberSignons", False)
        opts.set_preference("network.cookie.cookieBehavior", 1)
        driver = webdriver.Firefox(options=opts)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()
