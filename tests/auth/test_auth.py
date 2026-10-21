from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page import USERNAME_INPUT, PASSWORD_INPUT, LOGIN_BUTTON

def test_invalid_login(driver):
    """Сценарий 3: Неуспешная авторизация"""
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.CSS_SELECTOR, USERNAME_INPUT).send_keys("invalid_user")
    driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys("wrong_pass")
    driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()
    
    # Сообщение об ошибке
    error = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    
    assert "Username and password do not match" in error.text
