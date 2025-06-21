import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# 'pytest_addoption' is a specially named Pytest hook function. Pytest requires
# this exact function name in a conftest.py file to allow the addition of custom
# command-line options. When Pytest starts, it automatically discovers and calls
# any function with this name. Pytest passes a parser object to this function. The 
# parser is Pytest's built in tool for defining and processing these command-line 
# arguments. This particular implementation uses the hook to add a '--browser' option,
# enabling users to specify which browser to use when running the tests.
def pytest_addoption(parser):

    # Call the addoption function. The purpose of this function is to define a new command line option.
    parser.addoption(

        # Define the name of the command line option we are creating.
        # When a user runs tests, they will type pytest --browser chrome or pytest --browser firefox.
        "--browser",

        # This tells the parser what to do when it sees the --browser option on the command line.
        # "store" means when --browser is encountered, store the value that comes immediately after it.
        action="store",

        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests against"
    )

# Define a pytest fixture. This is a function that is ran before tests that request it. 
# scope="function" causes this fixture instance to be created once per test function
# The 'request' parameter is a special built in Pytest fixture that gives this 'driver'
# fixture information about the current test run, such as user-specified
# command-line options (in this case, which browser).
@pytest.fixture(scope="function")
def driver(request):

    # Get the value the user specified on the command line for which browser to use.
    browser = request.config.getoption("--browser")

    # If the browser to be used is Chrome, configure and initialize the Chrome WebDriver.
    if browser == "chrome":

        # Create an instance of ChromeOptions to customize Chrome's behavior.
        # Add an argument to run Chrome in headless mode (no visible UI window).
        # Add an argument to disable the GPU hardware acceleration.
        # This is often necessary when running in headless mode or in CI environments.
        # Add an argument to set the initial browser window size.
        # This is needed for testing responsive designs to ensure elements are rendered as expected.
        opts = ChromeOptions()
        opts.add_argument("--headless=new")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--window-size=1920,1080")
        
        # turn off the leak‑detection feature
        opts.add_argument("--disable-features=PasswordLeakDetection")

        # Disables Chrome’s new UI flag that triggers password leak detection UI changes.
        # Useful for suppressing popups related to breached passwords that may still appear
        # even if PasswordLeakDetection is disabled.
        opts.add_argument("--disable-features=PasswordLeakToggleMove")

        # opts.add_argument("--disable-blink-features=CredentialLeakDetection")
        # opts.add_argument("--disable-infobars")
        # opts.add_argument("--password-store=basic")

        # runs in guest mode, which appears to skip the dialog
        # opts.add_argument("--guest")


        # Disable Chrome's built-in password manager and "Save password?" prompts.
        # This is important in automation to prevent these pop-ups from interfering with
        # test execution. Also, disable third party cookies.
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,

            # Block third-party cookies but still allow first-party cookies,
            # minimizing cookie-consent dialogs and preventing external trackers from affecting tests.
            "profile.block_third_party_cookies": True,

            # Disables compromised password detection
             "profile.password_manager_leak_detection_enabled": False

        }

        # Apply the above dictionary of Chrome preferences to the browser options.
        opts.add_experimental_option("prefs", prefs)

        print("Initializing ChromeDriver using webdriver-manager...")

        # Attempt to initialize the ChromeDriver. This block includes error handling to catch any exceptions that may occur.
        try:

            # Create a ChromeService instance, which is responsible for managing the ChromeDriver executable.
            # The ChromeDriverManager().install() method downloads and installs the ChromeDriver executable if it's not already present.
            service = ChromeService(ChromeDriverManager().install())

            # Initialize the Chrome WebDriver instance, passing in the ChromeService instance and the ChromeOptions instance.
            driver = webdriver.Chrome(service=service, options=opts)
            print("ChromeDriver initialized successfully.")

        # Catch any exceptions that occur during ChromeDriver initialization and handle them accordingly.
        except Exception as e:

            # Log an error message with the exception details.
            # Fail the test setup using pytest.fail, passing in an error message with the exception details.
            print(f"Error initializing ChromeDriver: {e}")
            pytest.fail(f"Failed to initialize ChromeDriver: {e}")

    # Else if the Firefox browser is used.
    elif browser == "firefox":

        
        # Initialize FirefoxOptions, set it to run headlessly, and define a specific window size
        # for consistent test execution.
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        opts.add_argument("--width=1920")
        opts.add_argument("--height=1080")
        
        # disable the "Remember password" prompt.
        opts.set_preference("signon.rememberSignons", False)

        # Block third-party cookies but still allow first-party cookies,
        # minimizing cookie-consent dialogs and preventing external trackers from affecting tests.
        opts.set_preference("network.cookie.cookieBehavior", 1)

        print("Initializing GeckoDriver using webdriver-manager...")

        # Attempt to initialize the GeckoDriver. This block includes error handling to catch any exceptions that may occur.
        try:

            # Create a FirefoxService instance, which is responsible for managing the GeckoDriver executable.
            # The GeckoDriverManager().install() method downloads and installs the GeckoDriver executable if it's not already present.
            service = FirefoxService(GeckoDriverManager().install())

            # Initialize the Firefox WebDriver instance, passing in the FirefoxService instance and the FirefoxOptions instance.
            driver = webdriver.Firefox(service=service, options=opts)
            print("GeckoDriver initialized successfully.")

        # Catch any exceptions that occur during GeckoDriver initialization and handle them accordingly.
        except Exception as e:

            # Log an error message with the exception details.
            # Fail the test setup using pytest.fail, passing in an error message with the exception details.
            print(f"Error initializing GeckoDriver: {e}")
            pytest.fail(f"Failed to initialize GeckoDriver: {e}")

    else:
        # Handle unsupported browser choice
        error_message = f"Unsupported browser '{browser}' specified. Choose 'chrome' or 'firefox'."
        print(error_message)
        pytest.fail(error_message)

    # Set an implicit wait time of 10 seconds. This instructs WebDriver to wait
    # for up to 10 seconds when trying to find an element on the page. This gives the page time to load.
    driver.implicitly_wait(10)

    # Pauses the driver fixture and allows the test function to use the driver. Code prior to this
    # is the setup phase of the driver. Code after this, is the teardown phase of the driver.
    yield driver

    # Once the test function (or all tests within the fixture's scope) has completed, this closes 
    # all browser windows opened by this WebDriver instance and releases associated system resources.
    driver.quit()
