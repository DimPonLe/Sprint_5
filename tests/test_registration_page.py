import pytest
import random
import string
import locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

class TestRegistrationPage:
    @pytest.mark.parametrize("email_random_part_length, password_length", [
        (0, 6), 
        (1, 6),
        (30, 6),
        (10, 0),
        (10, 1),
        (10, 5),
        (10, 6),
        (10, 7),
        (10, 20)
    ])
    def test_register_with_email_lengths_and_different_password(self, registered_user, page_register):
        # Получаем данные пользователя из фикстуры
        user_data = registered_user
        # Авторизуемся
        page_register.find_element(*locators.ENTER_INPUT_EMAIL).send_keys(user_data["email"])  # поле Email
        page_register.find_element(*locators.ENTER_INPUT_PASSWORD).send_keys(user_data["password"])  # поле Пароль
        page_register.find_element(*locators.ENTER_BUTTON_LOG_IN).click()  # кнопка Войти
        WebDriverWait(page_register, 5).until(expected_conditions.text_to_be_present_in_element(locators.MAIN_BUTTON_ORDER, "Оформить заказ"))
        assert "Оформить заказ" in page_register.find_element(*locators.MAIN_BUTTON_ORDER).text