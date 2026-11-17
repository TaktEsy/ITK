"""
Задание: Напишите параметризованный декоратор @retry(max_attempts=3, delay=1).

Декоратор должен перехватывать любые исключения (Exception).
В случае ошибки он должен подождать delay секунд (с помощью time.sleep) и попробовать снова.
Если количество попыток max_attempts исчерпано, декоратор должен пробросить последнее исключение дальше.
Обязательно сохраните имя и docstring оригинальной функции (используйте functools.wraps).
"""
import functools
from logging import * 
import time

def retry(max_attempts: int = 3, delay: float = 1):
    # 2-й уровень: принимаем саму функцию
    def decorator(func):
        # Сохраняем имя и docstring оригинальной функции
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print(f"Попытка {attempt} из {max_attempts} не удалась. Ошибка: {err}")

                    if attempt == max_attempts:
                        #Если это была последняя попытка — пробрасываем ошибку дальше
                       
                       print(f"Все попытки исчерпаны.  {err}")

                    time.sleep(delay)

        return wrapper
    return decorator

@retry(2, 1)
def test():
    """Докстринг подопытной функции."""
    #print("Успешное срабатывание функции test")
    x = "RRRRRRR" / 2  
    return x

# 1. Имя и docstring
print("Имя функции в глобальном принте:", test.__name__)
print("Docstring в глобальном принте:", test.__doc__)

# 2. Запускаем функцию
test()