from selenium.webdriver.common.by import By

## Элементы со страницы регистрации

# поле Имя
REG_INPUT_NAME = (By.XPATH, ".//fieldset[1]//input")
# поле Email
REG_INPUT_EMAIL = (By.XPATH, ".//fieldset[2]//input")
# поле Пароль
REG_INPUT_PASSWORD = (By.NAME, "Пароль")
# кнопка Зарегистрироваться 
REG_BUTTON_LOG__IN = (By.XPATH, ".//button[text()='Зарегистрироваться']")
# сообщение Такой пользователь уже существует
REG_P_ERROR = (By.XPATH, "//p[contains(text(), 'Такой пользователь уже существует')]")


## Элементы со страницы входа

# заголовок Вход
ENTER_H2_LOGIN = (By.XPATH, ".//h2")
# поле Email
ENTER_INPUT_EMAIL = (By.XPATH, ".//input[@name='name']")
# поле Пароль
ENTER_INPUT_PASSWORD = (By.NAME, "Пароль")
# кнопка Войти
ENTER_BUTTON_LOG_IN = (By.XPATH, ".//button[text()='Войти']")
# надпись Восстановить пароль
ENTER_P_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")


## Элементы с главной страницы

# кнопка Оформить заказ
MAIN_BUTTON_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")
# заголовок Соберите бургер
MAIN_H1_ASSEMBLE_BURGER = (By.XPATH, ".//h1")
# кнопка Войти в аккаунт
MAIN_BUTTON_LOGIN_IN_ACCAUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")


## Элементы с личного кабинета

# текст в main В этом разделе вы можете изменить свои персональные данные
PRIV_P_HINT = (By.XPATH, ".//main//p")
# первый элемент списка-навигации в main Профиль
PRIV_A_PROFILE = (By.LINK_TEXT, "Профиль")
# кнопка Выход
PRIV_BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")


## элементы header

# текст в header Личный кабинет
HEAD_A_PRIVATE_CABINET = (By.XPATH, ".//nav/a")
# логотип Stellar Burgers
HEAD_SVG_STELLAR_BURGERS = (By.CSS_SELECTOR, '[xmlns="http://www.w3.org/2000/svg"]')
# первый элемент списка-навигации в header Конструктор
HEAD_P_CONSTRUCTOR = (By.XPATH, ".//nav//p")


## элементы со страницы Восстановление пароля
# заголовок восстановить пароль
RECOVER_H2_PASSWORD = (By.XPATH, ".//h2")
# поле Email
RECOVER_INPUT_EMAIL = (By.XPATH, ".//input[@name='name']")
# кнопка Восстановить
RECOVER_BUTTON_RECOVER = (By.XPATH, ".//button[text()='Восстановить']")
# поле Пароль
RECOVER_INPUT_CODE = (By.XPATH, ".//input[@name='Введите новый пароль']")
# кнопка Сохранить
RECOVER_BUTTON_SAVE = (By.XPATH, ".//button[text()='Сохранить']")
