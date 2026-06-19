def is_prime(num):
    """Проверка, является ли число простым"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    """Проверка, является ли число палиндромом"""
    s = str(num)
    return s == s[::-1]

# Ввод N
N = int(input("Введите N: "))

# Поиск палиндромных простых чисел
palindromes = []
for num in range(2, N + 1):
    if is_prime(num) and is_palindrome(num):
        palindromes.append(num)

# Вычисление среднего арифметического
if palindromes:
    average = sum(palindromes) / len(palindromes)
    print(f"{average:.2f}")  # Вывод с двумя знаками после запятой
else:
    print("0")

# Запись в файл
with open("palindromes.txt", "w") as file:
    for num in palindromes:
        file.write(str(num) + "\n")