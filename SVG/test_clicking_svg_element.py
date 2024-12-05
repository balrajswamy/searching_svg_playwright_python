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
    page.goto("https://www.amcharts.com/svg-maps/?map=india")
    page.wait_for_load_state("networkidle")
    time.sleep(3)  # Reduce unnecessary sleep time
    yield page  # Provide the page object to tests

    # Teardown
    context.close()
    browser.close()
    playwright.stop()  # Ensure Playwright is properly stopped

@pytest.mark.positive
def test_click_at_svg_search_button(setup_teardown):
    """
    this is working with selected date
    :param setup_teardown:
    :return:
    """
    page = setup_teardown
    title = page.evaluate("document.title")
    print(f"Page Title: {title}")
    time.sleep(3)
    # Scroll vertically to the 1000px position from the top of the page
    page.evaluate("window.scrollTo(0, 500)")

    print("Scrolled to 500px from the top of the page.")
    time.sleep(6)
    states_list = page.locator("//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    for state in states_list.element_handles():
        arial_label = state.get_attribute("aria-label")
        print("state_name=>", arial_label)
        if arial_label.strip() == "Delhi":
            state.click()
            break
    time.sleep(6)




