import random

# Ввод размера списка
N = int(input("Введите количество элементов N: "))

# Генерация списка из N случайных чисел от 1 до 100
numbers = [random.randint(1, 100) for _ in range(N)]

# Подсчёт суммы
total_sum = sum(numbers)

# Подсчёт количества чётных чисел
even_count = sum(1 for num in numbers if num % 2 == 0)

# Нахождение максимального элемента
maximum = max(numbers)

# Вывод результата
print(total_sum, even_count, maximum)