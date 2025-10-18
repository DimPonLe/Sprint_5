import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

# Тестируем разные длины пароля
@pytest.mark.parametrize("password_length", [0, 1, 5, 6, 7, 20])
def test_register_with_different_password_lengths(page_register, user_data, password_length):
    # Генерируем пароль указанной длины
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
    # Действия на странице регистрации
    page_register.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(user_data["name"])  # поле Имя
    page_register.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(user_data["email"])  # поле Email
    page_register.find_element(By.NAME, "Пароль").send_keys(password)  # поле Пароль
    page_register.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()  # кнопка Зарегистрироваться
    #Если имя уже зарегистрировано
    try:
        WebDriverWait(page_register, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Такой пользователь уже существует')]")))
        # Если сообщение появилось, меняем имя пользователя и повторяем попытку
        new_name = f"{user_data['name']}{random.randint(100, 999)}"
        user_data["name"] = new_name
        # Повторная попытка регистрации
        page_register.find_element(By.XPATH, ".//fieldset[1]//input").clear()
        page_register.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(new_name)  # новое имя
        page_register.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()  # кнопка Зарегистрироваться
    except TimeoutException:
        pass  # Если сообщение не появилось, продолжаем
    # Ждём заголовок Вход
    WebDriverWait(page_register, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//h2"), "Вход")) # второй заголовок Вход
    # Авторизуемся
    page_register.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(user_data["email"])  # поле Email
    page_register.find_element(By.NAME, "Пароль").send_keys(password)  # поле Пароль
    page_register.find_element(By.XPATH, ".//button[text()='Войти']").click()  # кнопка Войти
    # Ждём кнопку Оформить заказ
    WebDriverWait(page_register, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//section[2]//button"), "Оформить заказ"))
    # Проверяем, что заголовок Регистрация отсутствует
    assert page_register.find_element(By.XPATH, ".//h2").text != "Регистрация", "Заголовок 'Регистрация' остался на странице!"
