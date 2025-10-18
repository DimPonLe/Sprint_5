import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

# вход по кнопке «Войти в аккаунт» на главной c существующим в базе емэйлом и паролем
def test_button_go_in_accaunt_valid_existing_email_password_construction_section(page_home):
    page_home.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//h2"), "Вход")) # второй заголовок Вход
    page_home.find_element(By.XPATH, ".//fieldset[1]//input").send_keys("1234567890@ya.ru")  # поле Email
    page_home.find_element(By.NAME, "Пароль").send_keys("qwerty")  # поле Пароль
    page_home.find_element(By.XPATH, ".//button[text()='Войти']").click()  # кнопка Войти
    WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//section[2]//button"), "Оформить заказ"))
    assert page_home.find_element(By.XPATH, ".//h2").text != "Регистрация", "Заголовок 'Регистрация' остался на странице!"

# вход через кнопку «Личный кабинет»,
def test_button_private_page_login_valid_existing_email_password_construction_section(page_home):
    page_home.find_element(By.XPATH, ".//nav/a").click()
    WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//h2"), "Вход")) # второй заголовок Вход
    page_home.find_element(By.XPATH, ".//fieldset[1]//input").send_keys("1234567890@ya.ru")  # поле Email
    page_home.find_element(By.NAME, "Пароль").send_keys("qwerty")  # поле Пароль
    page_home.find_element(By.XPATH, ".//button[text()='Войти']").click()  # кнопка Войти
    WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//section[2]//button"), "Оформить заказ"))
    assert page_home.find_element(By.XPATH, ".//h2").text != "Регистрация", "Заголовок 'Регистрация' остался на странице!"

# вход через кнопку в форме регистрации
def test_register_with_different_password_lengths(page_register, user_data):
    # Генерируем пароль указанной длины
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    # Действия на странице регистрации
    page_register.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(user_data["name"])  # поле Имя
    page_register.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(user_data["email"])  # поле Email
    page_register.find_element(By.NAME, "Пароль").send_keys(password)  # поле Пароль
    page_register.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()  # кнопка Зарегистрироваться
    #Если имя уже зарегистрировано
    try:
        WebDriverWait(page_register, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Такой пользователь уже существует')]")))
        # Если сообщение появилось, меняем имя пользователя и повторяем попытку
        new_name = f"{user_data['name']} ({random.randint(100, 999)})"
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

# вход через кнопку в форме восстановления пароля.
def test_button_comeback_password_valid_existing_email_password_construction_section(page_home):
    page_home.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//h2"), "Вход")) # второй заголовок Вход
    page_home.find_element(By.XPATH, ".//p[2]").click()
    WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//h2"), "Восстановление пароля")) # второй заголовок Восстановление пароля
    page_home.find_element(By.XPATH, ".//fieldset//input").send_keys("1234567890@ya.ru")  # поле Email
    page_home.find_element(By.XPATH, ".//button[text()='Восстановить']").click()
    WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//fieldset[2]//label"), "Введите код из письма")) # второй плейсхолдер
    page_home.find_element(By.XPATH, ".//button[text()='Сохранить']").click()
    WebDriverWait(page_home, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//section[2]//button"), "Оформить заказ"))
    # Проверяем, что заголовок Восстановление пароля отсутствует
    assert page_home.find_element(By.XPATH, ".//h2").text != "Восстановление пароля"
