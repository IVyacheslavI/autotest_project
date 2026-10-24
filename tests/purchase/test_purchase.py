import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.suite("Покупка")
class TestPurchase:

    @allure.title("Успешная покупка")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.label("layer", "UI")
    def test_successful_purchase(self, logged_in_driver):
        """Сценарий 1: Успешная покупка"""
        driver = logged_in_driver

        with allure.step("Перейти в корзину"):
            driver.get("https://www.saucedemo.com/cart.html")

        with allure.step("Нажать Checkout"):
            checkout_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
            )
            checkout_btn.click()

        with allure.step("Заполнить личные данные"):
            first_name = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "first-name"))
            )
            first_name.send_keys("Ivan")
            driver.find_element(By.ID, "last-name").send_keys("Ivanov")
            driver.find_element(By.ID, "postal-code").send_keys("123456")

        with allure.step("Нажать Continue"):
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "continue"))
            ).click()

        with allure.step("Нажать Finish"):
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "finish"))
            ).click()

        with allure.step("Проверить успешное завершение"):
            complete_header = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
            )
            assert "Thank you for your order!" in complete_header.text
