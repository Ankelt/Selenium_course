from selenium import webdriver
import time
import math


def calc(digit):
    return str(math.log(abs(12 * math.sin(int(digit)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    # атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
    x = x_element.text
    y = calc(x)

    form = browser.find_element_by_id("answer")
    form.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
