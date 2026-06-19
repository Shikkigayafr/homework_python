import random

# ========== Задача 1 ==========
print("=== Задача 1 ===")
N = int(input("Введите количество элементов N: "))
numbers = [random.randint(1, 100) for _ in range(N)]
total_sum = sum(numbers)
even_count = sum(1 for num in numbers if num % 2 == 0)
maximum = max(numbers)
print(f"Сумма: {total_sum}, Чётных: {even_count}, Максимум: {maximum}\n")

# ========== Задача 2 ==========
print("=== Задача 2 ===")
s = input("Введите строку: ")
chars = []
counts = []

for ch in s:
    found = False
    for i in range(len(chars)):
        if chars[i] == ch:
            counts[i] += 1
            found = True
            break
    if not found:
        chars.append(ch)
        counts.append(1)

result = [f"{chars[i]}: {counts[i]}" for i in range(len(chars))]
print(", ".join(result))
print()

# ========== Задача 3 ==========
print("=== Задача 3 ===")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

N = int(input("Введите N: "))
palindromes = []

for num in range(2, N + 1):
    if is_prime(num) and is_palindrome(num):
        palindromes.append(num)

if palindromes:
    average = sum(palindromes) / len(palindromes)
    print(f"Среднее арифметическое: {average:.2f}")
else:
    print("Среднее арифметическое: 0")

# Запись в файл
with open("palindromes.txt", "w") as file:
    for num in palindromes:
        file.write(str(num) + "\n")

print(f"Найдено {len(palindromes)} палиндромных простых чисел. Результат сохранён в palindromes.txt")