import random

# Ввод размера матрицы
N = int(input("Введите размер матрицы N: "))

# Генерация случайной матрицы
A = [[random.randint(-20, 20) for _ in range(N)] for _ in range(N)]

# Вывод матрицы
print("\nСгенерированная матрица:")
for row in A:
    print(" ".join(f"{x:4d}" for x in row))

# Вычисление суммы и количества положительных элементов над главной диагональю
sum_positive = 0
count_positive = 0
above_diagonal = []

for i in range(N):
    for j in range(i + 1, N):
        above_diagonal.append(A[i][j])
        if A[i][j] > 0:
            sum_positive += A[i][j]
            count_positive += 1

# Вывод результатов
print("\n" + "=" * 50)
print("РЕЗУЛЬТАТЫ:")
print("=" * 50)
print(f"Элементы над главной диагональю: {above_diagonal}")
print(f"Количество всех элементов над диагональю: {len(above_diagonal)}")
print(f"Сумма положительных элементов: {sum_positive}")
print(f"Количество положительных элементов: {count_positive}")
print("=" * 50)