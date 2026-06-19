import random

# Загадываем число от 1 до 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Я загадал число от 1 до 100. У тебя 7 попыток!")

while attempts < max_attempts:
    guess = int(input("Введите число: "))
    attempts += 1
    
    if guess < secret_number:
        print("больше")
    elif guess > secret_number:
        print("меньше")
    else:
        print(f"Вы угадали за {attempts} попыток!")
        break
else:
    print(f"Попытки закончились. Загаданное число: {secret_number}")