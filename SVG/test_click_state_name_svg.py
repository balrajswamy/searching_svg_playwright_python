import pytest
import allure
from playwright.sync_api import sync_playwright, Page, expect
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
    page.goto("https://www.flipkart.com/")
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
    # searching for HP Laptops
    search_input = page.locator("//input[@name='q']")
    search_input.fill("HP Laptops")
    time.sleep(6)
    # click search button at SVG
    click_search_svg = page.locator("//button[@title='Search for Products, Brands and More']/*[name()='svg']")

    click_search_svg.evaluate("""(e1)=>{
                                    e1.style.border='2px solid red',
                                    e1.style.backgroundColr='yellow'
                                    }""")

    time.sleep(6)
    click_search_svg.click()


@pytest.mark.positive
def test_click_at_svg_state(setup_teardown):
    """
    this is working with selected date
    :param setup_teardown:
    :return:
    """
    page = setup_teardown
    title = page.evaluate("document.title")
    print(f"Page Title: {title}")
    time.sleep(3)
    # searching for HP Laptops

    time.sleep(6)
    # click search button at SVG
    click_search_svg = page.locator("//button[@title='Search for Products, Brands and More']/*[name()='svg']")

    click_search_svg.evaluate("""(e1)=>{
                                    e1.style.border='2px solid red',
                                    e1.style.backgroundColr='yellow'
                                    }""")

    time.sleep(6)
    click_search_svg.click()

