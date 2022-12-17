import time
from selenium.webdriver.common.by import By


def test_search_example(browser):
    """Search some phrase in google and make a screenshot of the page."""

    # Open google search page:
    browser.get("https://google.com")

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for search text input:
    search_input = browser.find_element(By.NAME, "q")

    # Enter the text for search:
    search_input.clear()
    search_input.send_keys("first test")

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search:
    search_button = browser.find_element(By.NAME, "btnK")
    search_button.click()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    browser.save_screenshot("result.png")
