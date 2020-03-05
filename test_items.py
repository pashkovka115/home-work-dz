# В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину.
# Тест должен запускаться с параметром language следующей командой: pytest --language=es test_items.py
# и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.

# Комманды для проверки
# pytest --language=es test_items.py
# pytest --language=es
# pytest --language=fr


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_language(browser):
    browser: webdriver.Chrome
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    browser.get(link)
    sleep(3) # что бы визуально успеть увидеть

    # Ждём появления кнопки (на всякий случай)
    button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#add_to_basket_form button[type="submit"]'))
    )

    assert button, f'Нет кнопки добавления в корзину на странице: {link}'


