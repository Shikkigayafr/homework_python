# Ввод строки
text = input("Введите русскоязычный текст: ")

# Очистка от знаков препинания
import string
for punct in string.punctuation:
    text = text.replace(punct, ' ')

# Разбиваем на слова и считаем
words = text.split()
count = sum(1 for word in words if word.lower().startswith('е'))

print(f"Количество слов, начинающихся с буквы 'е': {count}")