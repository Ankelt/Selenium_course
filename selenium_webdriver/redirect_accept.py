import time
from selenium import webdriver
import math


def calc(digit):
    return str(math.log(abs(12 * math.sin(int(digit)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    form = browser.find_element_by_id("answer")
    form.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
