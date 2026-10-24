import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.inventory_page import ADD_TO_CART_BUTTON, SHOPPING_CART_LINK
from locators.cart_page import CART_ITEM, REMOVE_BUTTON, CONTINUE_SHOPPING_BUTTON

@allure.suite("Корзина")
class TestCart:

    @allure.title("Очищение корзины")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("layer", "UI")
    def test_clear_cart(self, logged_in_driver):
        """Сценарий 2: Очищение корзины"""
        driver = logged_in_driver

        with allure.step("Добавить товар в корзину"):
            add_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ADD_TO_CART_BUTTON))
            )
            add_btn.click()

        with allure.step("Перейти в корзину"):
            cart_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, SHOPPING_CART_LINK))
            )
            cart_link.click()

        with allure.step("Проверить наличие товара"):
            cart_items = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, CART_ITEM))
            )
            assert len(cart_items) == 1, "Товар не появился в корзине"

        with allure.step("Удалить товар"):
            remove_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, REMOVE_BUTTON))
            )
            remove_btn.click()

        with allure.step("Проверить, что корзина пуста"):
            cart_items_after = driver.find_elements(By.CSS_SELECTOR, CART_ITEM)
            assert len(cart_items_after) == 0, "Корзина не очистилась"

        with allure.step("Вернуться на страницу товаров"):
            continue_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, CONTINUE_SHOPPING_BUTTON))
            )
            continue_btn.click()
            assert "inventory.html" in driver.current_url
