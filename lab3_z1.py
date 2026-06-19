# Ввод трёх целых чисел
a = int(input("Введите первое целое число (a): "))
b = int(input("Введите второе целое число (b): "))
c = int(input("Введите третье целое число (c): "))

# Проверка каждого числа
print("\nРезультаты проверки:")
print("-" * 35)

def check_number(num, name):
    """Проверяет число и возвращает строку с результатом"""
    if 1 <= num <= 3:
        return f"{name} = {num} -> ПРИНАДЛЕЖИТ [1, 3] ✓"
    else:
        return f"{name} = {num} -> НЕ ПРИНАДЛЕЖИТ [1, 3] ✗"

# Вывод проверки для каждого числа
print(check_number(a, "a"))
print(check_number(b, "b"))
print(check_number(c, "c"))

# Сбор подходящих чисел
selected = []
if 1 <= a <= 3:
    selected.append(a)
if 1 <= b <= 3:
    selected.append(b)
if 1 <= c <= 3:
    selected.append(c)

# Итоговый вывод
print("\n" + "=" * 35)
if selected:
    print(f"Выбраны числа: {', '.join(map(str, selected))}")
else:
    print("Подходящих чисел не найдено")