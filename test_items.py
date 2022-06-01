from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_the_shopping_cart_button(browser):
    browser.get(link)
    bas_text = browser.find_element(By.CSS_SELECTOR, value=".btn-lg").text
    print(bas_text)
    assert bas_text, "Texts do not match"


# pytest -s -v --language=fr test_items.py