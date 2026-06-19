# Ввод размера массива
N = int(input("Введите количество элементов массива N: "))

# Создание пустого массива
array = []

# Ввод элементов массива
print("Введите элементы массива:")
for i in range(N):
    element = int(input(f"Элемент {i+1}: "))
    array.append(element)

# Поиск максимального элемента
max_element = array[0]  # предполагаем, что первый элемент максимальный
for i in range(1, N):
    if array[i] > max_element:
        max_element = array[i]

# Вывод результатов
print("\n" + "=" * 40)
print("РЕЗУЛЬТАТЫ:")
print("=" * 40)
print(f"Исходный массив: {array}")
print(f"Максимальный элемент: {max_element}")

# Вывод массива в обратном порядке
reversed_array = array[::-1]  # срез с шагом -1
print(f"Массив в обратном порядке: {reversed_array}")
print("=" * 40)