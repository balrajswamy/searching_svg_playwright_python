import pytest
import allure
from playwright.sync_api import sync_playwright, Page,expect
import time
import os


@pytest.fixture(scope="function")
def setup_teardown():
    """Fixture to initialize and teardown Playwright browser and page."""
    playwright = sync_playwright().start()  # Start Playwright
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Load the login page
    page.goto("https://playwright.dev/python/docs/videos")
    page.wait_for_load_state("networkidle")
    time.sleep(3)  # Reduce unnecessary sleep time
    yield page  # Provide the page object to tests

    # Teardown
    context.close()
    browser.close()
    playwright.stop()  # Ensure Playwright is properly stopped

@pytest.mark.positive
def test_with_javascript(setup_teardown):
    """
    this is working with selected date
    :param setup_teardown:
    :return:
    """
    page = setup_teardown
    title = page.evaluate("document.title")
    print(f"Page Title: {title}")
    time.sleep(3)
    script = """(message)=>{return message;}
                """
    result = page.evaluate(script,"Hello Playwright")
    print("result:\t", result)
    time.sleep(6)
