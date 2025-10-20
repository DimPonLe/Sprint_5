import random
import string
import pytest
import urls
import locators
import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from names import NAMES

# Фикстура для браузера
@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1280,720')
    chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

# Фикстура для страницы регистрации
@pytest.fixture()
def page_register(browser):
    browser.get(urls.REGISTER_URL)
    return browser

#Фикстура для домашней страницы
@pytest.fixture()
def page_home(browser):
    browser.get(urls.HOME_URL)
    return browser

#Фикстура для захода в личный кабинет
@pytest.fixture()
def logged_in_account(page_home):
    # Переход на страницу входа
    page_home.find_element(*locators.ENTER_BUTTON_LOGIN_IN_ACCAUNT).click()
    WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element(*locators.ENTER_H2_LOGIN, "Вход"))
    # Ввод данных пользователя
    page_home.find_element(*locators.ENTER_INPUT_EMAIL).send_keys(data.TEST_EMAIL)  # поле Email
    page_home.find_element(*locators.ENTER_INPUT_PASSWORD).send_keys(data.TEST_PASSWORD)  # поле Пароль
    page_home.find_element(*locators.ENTER_BUTTON_LOG_IN).click()  # кнопка Войти
    WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element(*locators.MAIN_BUTTON_ORDER, "Оформить заказ"))
    return page_home

#Фикстура для работы в личном кабинете
@pytest.fixture()
def private_page(logged_in_account):
    logged_in_account.find_element(*locators.HEAD_A_PRIVATE_CABINET).click() #  кнопка "Личный кабинет"
    WebDriverWait(logged_in_account, 5).until(expected_conditions.text_to_be_present_in_element(*locators.PRIV_P_HINT, "В этом разделе вы можете изменить свои персональные данные"))
    return logged_in_account

# Фикстура для регистрации пользователя
@pytest.fixture()
def registered_user(page_register, password_length, email_random_part_length):
    name = random.choice(NAMES)

    # Генерируем случайную часть email с заданной длиной
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=email_random_part_length))
    domain = random.choice(["@mail.ru", "@yandex.ru", "@gmail.com", "@rambler.ru"])
    email = f"{random_part}{domain}"

    # Генерируем пароль указанной длины
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))

    # Действия на странице регистрации
    page_register.find_element(*locators.REG_INPUT_NAME).send_keys(name)  # поле Имя
    page_register.find_element(*locators.REG_INPUT_EMAIL).send_keys(email)  # поле Email
    page_register.find_element(*locators.REG_INPUT_PASSWORD).send_keys(password)  # поле Пароль
    page_register.find_element(*locators.REG_BUTTON_LOG__IN).click()  # кнопка Зарегистрироваться

    # Инициализируем new_name вне блока try-except
    new_name = None

    # Если имя уже зарегистрировано
    try:
        WebDriverWait(page_register, 3).until(expected_conditions.visibility_of_element_located(locators.REG_P_ERROR))
        # Если сообщение появилось, меняем имя пользователя и повторяем попытку
        new_name = f"{name}{random.randint(100, 999)}"
        page_register.find_element(*locators.REG_INPUT_NAME).clear()
        page_register.find_element(*locators.REG_INPUT_NAME).send_keys(new_name)  # новое имя
        page_register.find_element(*locators.REG_BUTTON_LOG__IN).click()  # кнопка Зарегистрироваться
    except TimeoutException:
        pass  # Если сообщение не появилось, продолжаем

    # Ждём заголовок Вход на странице Входа
    WebDriverWait(page_register, 5).until(expected_conditions.text_to_be_present_in_element(locators.ENTER_H2_LOGIN, "Вход"))

    # Возвращаем данные для дальнейшего использования
    return {
        "password": password,
        "email": email,
        "name": new_name or name  # Если new_name не было установлено, используем исходное имя
    }