def test_basket_is_present(browser):
    browser.implicitly_wait(15)
    answer_locate = browser.find_element_by_id("add_to_basket_form")
    assert answer_locate, "Element for adding in basket is not present"

