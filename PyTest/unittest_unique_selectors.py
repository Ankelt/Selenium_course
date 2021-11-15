from selenium import webdriver
import time
import unittest


def get_welcome_text(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(".first_block .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".first_block .third")
    input3.send_keys("Ivanov@notmail.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # закрываем браузер после всех манипуляций
    browser.quit()

    return welcome_text


class TestSelectors(unittest.TestCase):
    def test_selectors1(self):
        welcome_text = get_welcome_text("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text, "Registration failed")

    def test_selectors2(self):
        welcome_text = get_welcome_text("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text, "Registration failed")


if __name__ == '__main__':
    unittest.main()
