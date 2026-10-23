import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page import USERNAME_INPUT, PASSWORD_INPUT, LOGIN_BUTTON

@allure.suite("Авторизация")
class TestAuth:

    @allure.title("Неуспешная авторизация")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("layer", "UI")
    def test_invalid_login(self, driver):
        """Сценарий 3: Неуспешная авторизация"""
        with allure.step("Открыть страницу авторизации"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Ввести неверный логин и пароль"):
            driver.find_element(By.CSS_SELECTOR, USERNAME_INPUT).send_keys("invalid_user")
            driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys("wrong_pass")

        with allure.step("Нажать кнопку Login"):
            driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()

        with allure.step("Проверить сообщение об ошибке"):
            error = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
            )
            assert "Username and password do not match" in error.text
