import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"


def test_item_page_contains_button_add_to_cart(browser):
    browser.get(link)

    buttons = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".btn-add-to-basket")))

    # Wait to see the language
    time.sleep(5)

    assert len(buttons) > 0, "Button not found!"
