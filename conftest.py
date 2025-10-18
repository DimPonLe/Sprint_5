import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from names import NAMES

# Фикстура для данных пользователя
@pytest.fixture()
def user_data():
    name = random.choice(NAMES)
    email = f"{random.randint(100, 999)}@ya.ru"
    return {"name": name, "email": email}

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
    browser.get("https://stellarburgers.education-services.ru/register")
    return browser

#Фикстура для домашней страницы
@pytest.fixture()
def page_home(browser):
    browser.get("https://stellarburgers.education-services.ru")
    return browser

#Фикстура для захода в личный кабинет
@pytest.fixture()
def logged_in_account(page_home):
    # Переход на страницу входа
    page_home.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//h2"), "Вход"))
    # Ввод данных пользователя
    page_home.find_element(By.XPATH, ".//fieldset[1]//input").send_keys("1234567890@ya.ru")  # поле Email
    page_home.find_element(By.NAME, "Пароль").send_keys("qwerty")  # поле Пароль
    page_home.find_element(By.XPATH, ".//button[text()='Войти']").click()  # кнопка Войти
    WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//section[2]//button"), "Оформить заказ"))
    return page_home

#Фикстура для работы в личном кабинете
@pytest.fixture()
def private_page(logged_in_account):
    logged_in_account.find_element(By.XPATH, ".//nav/a").click() #  кнопка "Личный кабинет"
    WebDriverWait(logged_in_account, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//main//p"), "В этом разделе вы можете изменить свои персональные данные"))
    return logged_in_account