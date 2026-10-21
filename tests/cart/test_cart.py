from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.inventory_page import ADD_TO_CART_BUTTON, SHOPPING_CART_LINK
from locators.cart_page import CART_ITEM, REMOVE_BUTTON, CONTINUE_SHOPPING_BUTTON

def test_clear_cart(logged_in_driver):
    """Сценарий 2: Очищение корзины"""
    driver = logged_in_driver
    
    # Нажимаем на кнопку "Add to cart"
    add_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ADD_TO_CART_BUTTON))
    )
    add_btn.click()
    
    # Переходим в корзину
    cart_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, SHOPPING_CART_LINK))
    )
    cart_link.click()
    
    # Проверяем появление товара в корзине
    cart_items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, CART_ITEM))
    )
    assert len(cart_items) == 1, "Товар не появился в корзине"
    
    # Удаляем товар из корзины
    remove_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, REMOVE_BUTTON))
    )
    remove_btn.click()
    
    # Проверяем, что корзина пуста
    cart_items_after = driver.find_elements(By.CSS_SELECTOR, CART_ITEM)
    assert len(cart_items_after) == 0, "Корзина не очистилась"
    
    # Переходим в каталог товаров
    continue_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, CONTINUE_SHOPPING_BUTTON))
    )
    continue_btn.click()
    assert "inventory.html" in driver.current_url
