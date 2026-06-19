name = input("Введите имя: ")
age = int(input("Введите возраст: "))

# Проверка имени
if not name.isalpha() or not (2 <= len(name) <= 30):
    print("Некорректное имя")
# Проверка возраста
elif age < 0:
    print("Некорректный возраст")
else:
    print("OK")