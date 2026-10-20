# Складываем числа
def add_numbers(*args):
    return sum(args)

# Используем фикстуру numbers с набором чисел из confest.py
def test_add_numbers(numbers):
        
    # Ожидаемый результат
    expected_result = sum(numbers)
    
    # Фактический результат
    actual_result = add_numbers(*numbers)
    
    # Проверка совпадения результатов
    assert actual_result == expected_result, f"Ошибка при сложении {numbers}"
