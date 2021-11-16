import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('steps', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_send_answer_by_link(browser, steps):
    link = f"https://stepik.org/lesson/{steps}/step/1"
    browser.get(link)
    browser.implicitly_wait(15)
    answer_locate = browser.find_element_by_css_selector("textarea")
    key = str(math.log(int(time.time())))
    answer_locate.send_keys(key)
    button_clickable = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    if button_clickable:
        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()
        browser.implicitly_wait(15)
        answer = browser.find_element_by_css_selector("pre.smart-hints__hint")
        answer_text = answer.text
        assert answer_text == "Correct!", "Something went wrong"
