import time
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(digit):
    return str(math.log(abs(12 * math.sin(int(digit)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_clickable = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), text_="$100")
    )
    if button_clickable:
        button = browser.find_element_by_id("book")
        button.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    form = browser.find_element_by_id("answer")
    form.send_keys(y)

    accept = browser.find_element_by_id("solve")
    accept.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
