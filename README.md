# QA Automation Portfolio: Swag Labs E-commerce Site

This project contains automated UI tests for the Swag Labs demo e-commerce website (https://www.saucedemo.com). It demonstrates UI test automation using Python, Selenium WebDriver, and the Pytest framework, structured with the Page Object Model (POM) design pattern.

## Table of Contents

- [Features Tested](#features-tested)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Tests](#running-the-tests)
- [Project Structure](#project-structure)
- [Notes on Specific Implementations](#notes-on-specific-implementations)

## Features Tested

This test suite covers the following core functionalities of the Swag Labs website:

*   **Login:**
    *   Successful login with valid "standard_user" credentials.
    *   Verification of error messages for invalid login attempts.
*   **Product Interaction:**
    *   Adding specific products to the shopping cart from the products page.
    *   Removing products from the cart.
    *   Verifying the cart badge count updates correctly after adding an item.
*   **Shopping Cart:**
    *   Verifying that an empty cart correctly shows no items.
    *   Verifying that added items appear correctly in the cart.
    *   Verifying the subtotal from item prices in the cart.
*   **Checkout Process:**
    *   Proceeding from cart to checkout.
    *   Entering customer information (first name, last name, postal code).
    *   Proceeding to the checkout overview page.
    *   Verifying item names on the checkout overview page.
    *   Verifying that the subtotal ("Item total") on the overview page matches the sum of item prices.
    *   Completing the purchase by clicking "Finish".
*   **Order Confirmation:**
    *   Verifying the "Thank you for your order!" confirmation message on the final page.

## Tech Stack

*   **Language:** Python
*   **Automation Library:** Selenium WebDriver (see `requirements.txt`)
*   **Testing Framework:** Pytest
*   **Design Pattern:** Page Object Model (POM)
*   **Browser Driver Management:** `webdriver-manager` (used within `conftest.py` for Chrome/Firefox driver setup)
*   **Dependency Management:** `pip` with `requirements.txt`

## Prerequisites

*   Python 3.9 or newer recommended.
*   `pip` (Python package installer).
*   Google Chrome browser installed.
*   (Optional) Mozilla Firefox browser installed (if using the `--browser firefox` option).

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone git@github.com:jdwright963/selenium-pytest-swag-labs.git
    cd selenium-pytest-swag-labs
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv env
    ```
    *   Windows: `.\env\Scripts\activate`
    *   macOS/Linux: `source env/bin/activate`

3.  **Install Dependencies:**
    From the project root directory (where `requirements.txt` is located):
    ```bash
    pip install -r requirements.txt
    ```
    This command installs all necessary packages including Selenium, Pytest, and their dependencies.

4.  **Browser Drivers:**
    This project uses `webdriver-manager` (configured in `conftest.py`) to automatically download and manage the appropriate WebDriver (e.g., ChromeDriver, GeckoDriver) for your installed browser version. An internet connection is required the first time tests are run for the driver download.

## Running the Tests

1.  Ensure your virtual environment is activated.
2.  Navigate to the project's root directory in your terminal.
3.  **Run all tests:**
    ```bash
    pytest
    ```
    For more detailed output:
    ```bash
    pytest -v
    ```

4.  **Specify Browser (Optional):**
    The tests can be run against different browsers if configured in `conftest.py` (current setup supports Chrome and Firefox).
    ```bash
    pytest --browser chrome  # Default
    pytest --browser firefox
    ```

5.  **Run specific test files or tests:**
    ```bash
    pytest tests/test_shopping_flow.py  # Run all tests in a specific file
    pytest -k test_complete_checkout_flow # Run a specific test by name
    ```