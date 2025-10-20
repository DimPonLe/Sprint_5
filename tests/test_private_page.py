import pytest
import locators
import urls
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestPrivatePage:
    # авторизировался, нажал на текст «Личный кабинет»
    def test_button_private_page_succesfull_loggin(self, logged_in_account):   
        logged_in_account.find_element(*locators.HEAD_A_PRIVATE_CABINET).click() #  текст "Личный кабинет"
        WebDriverWait(logged_in_account, 5).until(expected_conditions.text_to_be_present_in_element(locators.PRIV_P_HINT, "В этом разделе вы можете изменить свои персональные данные"))
        assert logged_in_account.find_element(*locators.PRIV_A_PROFILE).text == "Профиль"

    # авторизировался, переход по клику на «Конструктор» и на логотип Stellar Burgers.
    def test_click_text_Constructor_(self, private_page):
        private_page.find_element(*locators.HEAD_P_CONSTRUCTOR).click() #  текст "Конструктор"
        WebDriverWait(private_page, 5).until(expected_conditions.text_to_be_present_in_element(locators.MAIN_BUTTON_ORDER, "Оформить заказ"))
        assert private_page.find_element(*locators.MAIN_H1_ASSEMBLE_BURGER).text == "Соберите бургер"

    def test_click_logo(self, private_page): 
        private_page.find_element(*locators.HEAD_SVG_STELLAR_BURGERS).click() #  логотип Stellar Burgers
        WebDriverWait(private_page, 5).until(expected_conditions.text_to_be_present_in_element(locators.MAIN_BUTTON_ORDER, "Оформить заказ"))
        assert private_page.find_element(*locators.MAIN_H1_ASSEMBLE_BURGER).text == "Соберите бургер"

    # авторизировался, нажимаю на "Выход"
    def test_button_exit(self, logged_in_account):   
        logged_in_account.find_element(*locators.HEAD_A_PRIVATE_CABINET).click() #  текст Личный кабинет
        WebDriverWait(logged_in_account, 5).until(expected_conditions.text_to_be_present_in_element(locators.PRIV_P_HINT, "В этом разделе вы можете изменить свои персональные данные"))
        logged_in_account.find_element(*locators.PRIV_BUTTON_EXIT).click() #  кнопка "Выход"
        WebDriverWait(logged_in_account, 5).until(expected_conditions.text_to_be_present_in_element(locators.ENTER_H2_LOGIN, "Вход")) # второй заголовок Вход
        url_login = logged_in_account.current_url 
        assert url_login == urls.LOGIN_URL