s = input("Введите строку: ")

# Списки для хранения символов и их количества
chars = []
counts = []

# Проходим по каждому символу
for ch in s:
    # Проверяем, встречался ли уже этот символ
    found = False
    for i in range(len(chars)):
        if chars[i] == ch:
            counts[i] += 1
            found = True
            break
    
    # Если не встречался - добавляем новый
    if not found:
        chars.append(ch)
        counts.append(1)

# Вывод результата
result = []
for i in range(len(chars)):
    result.append(f"{chars[i]}: {counts[i]}")
print(", ".join(result))