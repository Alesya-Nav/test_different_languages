import time
from selenium.webdriver.common.by import By

def test_add_to_cart_button_is_present(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Задержка для проверки текста кнопки вручную
    time.sleep(30)

    # Проверяем наличие кнопки добавления в корзину
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_cart_button, "Кнопка добавления в корзину отсутствует"
