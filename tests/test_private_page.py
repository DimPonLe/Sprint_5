import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# авторизировался, нажал на текст «Личный кабинет»
def test_button_private_page_succesfull_loggin(logged_in_account):   
    logged_in_account.find_element(By.XPATH, ".//nav/a").click() #  текст "Личный кабинет"
    WebDriverWait(logged_in_account, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//main//p"), "В этом разделе вы можете изменить свои персональные данные"))
    assert logged_in_account.find_element(By.LINK_TEXT, "Профиль").text == "Профиль"

# авторизировался, переход по клику на «Конструктор» и на логотип Stellar Burgers.
def test_click_text_Constructor_(private_page):
    private_page.find_element(By.XPATH, ".//nav//p").click() #  текст "Конструктор"
    WebDriverWait(private_page, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//section[2]//button"), "Оформить заказ"))
    assert private_page.find_element(By.XPATH, ".//h1").text == "Соберите бургер"

def test_click_logo(private_page): 
    private_page.find_element(By.CSS_SELECTOR, '[xmlns="http://www.w3.org/2000/svg"]').click() #  логотип Stellar Burgers
    WebDriverWait(private_page, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//section[2]//button"), "Оформить заказ"))
    assert private_page.find_element(By.XPATH, ".//h1").text == "Соберите бургер"

# авторизировался, нажимаю на "Выход"
def test_button_exit(logged_in_account):   
    logged_in_account.find_element(By.XPATH, ".//nav/a").click() #  текст "Выход"
    WebDriverWait(logged_in_account, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//main//p"), "В этом разделе вы можете изменить свои персональные данные"))
    logged_in_account.find_element(By.XPATH, ".//button[text()='Выход']").click() #  кнопка "Выход"
    WebDriverWait(logged_in_account, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ".//h2"), "Вход")) # второй заголовок Вход
    url_login = logged_in_account.current_url 
    assert url_login == "https://stellarburgers.education-services.ru/login"