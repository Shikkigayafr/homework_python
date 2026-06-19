# Ввод первого массива
print("Введите первый массив:")
n1 = int(input("Количество элементов (не более 15): "))
array1 = []
for i in range(n1):
    array1.append(int(input(f"Элемент {i+1}: ")))

# Ввод второго массива
print("\nВведите второй массив:")
n2 = int(input("Количество элементов (не более 15): "))
array2 = []
for i in range(n2):
    array2.append(int(input(f"Элемент {i+1}: ")))

# Ввод третьего массива
print("\nВведите третий массив:")
n3 = int(input("Количество элементов (не более 15): "))
array3 = []
for i in range(n3):
    array3.append(int(input(f"Элемент {i+1}: ")))

# Функция для вычисления суммы и среднего
def calculate_stats(arr):
    """Вычисляет сумму и среднее арифметическое массива"""
    if len(arr) == 0:
        return 0, 0
    total = sum(arr)
    average = total / len(arr)
    return total, average

# Вычисление для каждого массива
sum1, avg1 = calculate_stats(array1)
sum2, avg2 = calculate_stats(array2)
sum3, avg3 = calculate_stats(array3)

# Вывод результатов
print("\n" + "=" * 60)
print("РЕЗУЛЬТАТЫ:")
print("=" * 60)

print(f"\nПервый массив: {array1}")
print(f"  Сумма: {sum1}")
print(f"  Среднее арифметическое: {avg1:.2f}")

print(f"\nВторой массив: {array2}")
print(f"  Сумма: {sum2}")
print(f"  Среднее арифметическое: {avg2:.2f}")

print(f"\nТретий массив: {array3}")
print(f"  Сумма: {sum3}")
print(f"  Среднее арифметическое: {avg3:.2f}")

print("=" * 60)