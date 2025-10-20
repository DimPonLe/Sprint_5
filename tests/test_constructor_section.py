import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestConstructorSection:
# проверка перехода в Булки, Соусы, Начинки через скроллинг
    @pytest.mark.parametrize("index,text", [(1, "Булки"), (2, "Соусы"), (3, "Начинки")])
    def test_scrolling_bread_sauce_topping(self, logged_in_account, index, text): 
        element = logged_in_account.find_element(By.XPATH, f".//main//h2[{index}]") # заголовки h2 Булки, Соусы, Начинки
        logged_in_account.execute_script("arguments[0].scrollIntoView();", element)
        assert element.text == text, f"Ожидается заголовок '{text}', а отображается '{element.text}'"

    # проверка перехода в Соусы, Начинки через нажание на текст
    @pytest.mark.parametrize("text", ["Соусы", "Начинки"])
    def test_click_text_bread_sauce_topping(self, logged_in_account, text):
        # Находим элемент по тексту и кликаем на него
        element = logged_in_account.find_element(By.XPATH, f".//div/span[text()='{text}']").click()
        # Проверяем, что после клика отображается нужный заголовок
        assert logged_in_account.find_element(By.XPATH, f".//main//h2[text()='{text}']").text == text, \
            f"Ожидается заголовок '{text}', а отображается другой"