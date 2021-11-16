link = "http://selenium1py.pythonanywhere.com/"


# фикстура, находящаяся в той же директории или выше, подгружается в качестве параметра
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")