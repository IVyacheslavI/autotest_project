import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from locators.login_page import USERNAME_INPUT, PASSWORD_INPUT, LOGIN_BUTTON


@pytest.fixture
def driver():
    """Фикстура для запуска и закрытия браузера"""
    chrome_options = Options()
    
    # Отключаем всплывающие окна
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    
    # Дополнительные флаги
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--incognito")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    """Фикстура для авторизации на сайте"""
    driver.get("https://www.saucedemo.com/")
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, USERNAME_INPUT))
    ).send_keys("standard_user")
    
    driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()
    
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
    return driver
