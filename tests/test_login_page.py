import random
import string
import locators
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

class TestLoginPage:
    # вход по кнопке «Войти в аккаунт» на главной c существующим в базе емэйлом и паролем
    def test_button_go_in_accaunt_valid_existing_email_password_construction_section(safe, page_home):
        page_home.find_element(locators.BUTTON_LOGIN_IN_ACCAUNT).click()
        WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element(*locators.H2_LOGIN, "Вход")) # второй заголовок Вход
        page_home.find_element(locators.ENTER_INPUT_EMAIL).send_keys(data.TEST_EMAIL)  # поле Email
        page_home.find_element(locators.ENTER_INPUT_PASSWORD).send_keys(data.TEST_PASSWORD)  # поле Пароль
        page_home.find_element(locators.ENTER_BUTTON_LOG_IN).click()  # кнопка Войти
        WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element(*locators.MAIN_BUTTON_ORDER, "Оформить заказ"))
        assert "Оформить заказ" in page_home.find_element(*locators.MAIN_BUTTON_ORDER).text

    # вход через кнопку «Личный кабинет»,
    def test_button_private_page_login_valid_existing_email_password_construction_section(self, page_home):
        page_home.find_element(*locators.HEAD_A_PRIVATE_CABINET).click()
        WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element(locators.ENTER_H2_LOGIN, "Вход")) # второй заголовок Вход
        page_home.find_element(*locators.ENTER_INPUT_EMAIL).send_keys(data.TEST_EMAIL)  # поле Email
        page_home.find_element(*locators.ENTER_INPUT_PASSWORD).send_keys(data.TEST_PASSWORD)  # поле Пароль
        page_home.find_element(*locators.ENTER_BUTTON_LOG_IN).click()  # кнопка Войти
        WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element(locators.MAIN_BUTTON_ORDER, "Оформить заказ"))
        assert "Оформить заказ" in page_home.find_element(*locators.MAIN_BUTTON_ORDER).text

    # вход через кнопку в форме регистрации
    def test_button_login_from_registration(self, registered_user, page_register):
        email_random_part_length = 10
        password_length = 6
        # Получаем данные пользователя из фикстуры
        user_data = registered_user(page_register, password_length, email_random_part_length)
        # Авторизуемся
        page_register.find_element(*locators.ENTER_INPUT_EMAIL).send_keys(user_data["email"])  # поле Email
        page_register.find_element(*locators.ENTER_INPUT_PASSWORD).send_keys(user_data["password"])  # поле Пароль
        page_register.find_element(*locators.ENTER_BUTTON_LOG_IN).click()  # кнопка Войти
        WebDriverWait(page_register, 5).until(expected_conditions.text_to_be_present_in_element(locators.MAIN_BUTTON_ORDER, "Оформить заказ"))
        assert "Оформить заказ" in page_register.find_element(*locators.MAIN_BUTTON_ORDER).text
   
    # вход через кнопку в форме восстановления пароля.
    def test_button_comeback_password_valid_existing_email_password_construction_section(self, page_home):
        page_home.find_element(*locators.MAIN_BUTTON_LOGIN_IN_ACCAUNT).click()
        WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element(locators.ENTER_H2_LOGIN, "Вход")) # второй заголовок Вход
        page_home.find_element(*locators.ENTER_P_PASSWORD).click() # надпись Восстановить пароль
        WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element(locators.RECOVER_H2_PASSWORD, "Восстановление пароля")) # второй заголовок Восстановление пароля
        page_home.find_element(*locators.RECOVER_INPUT_EMAIL).send_keys(data.TEST_EMAIL)  # поле Email
        page_home.find_element(*locators.RECOVER_BUTTON_RECOVER).click()
        WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element(locators.RECOVER_INPUT_CODE, "Введите код из письма")) # второй плейсхолдер
        page_home.find_element(*locators.RECOVER_BUTTON_SAVE).click()
        WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element(locators.MAIN_BUTTON_ORDER, "Оформить заказ"))
        assert "Оформить заказ" in page_home.find_element(*locators.MAIN_BUTTON_ORDER).text