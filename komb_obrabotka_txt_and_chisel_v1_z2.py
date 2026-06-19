date_str = input("Введите дату в формате ДД.ММ.ГГГГ: ")

# Проверка формата (10 символов и точки на 3-й и 6-й позициях)
if len(date_str) != 10 or date_str[2] != '.' or date_str[5] != '.':
    print("Некорректная дата")
else:
    # Разбиваем строку на части
    try:
        day = int(date_str[0:2])
        month = int(date_str[3:5])
        year = int(date_str[6:10])
    except ValueError:
        print("Некорректная дата")
        exit()
    
    # Проверка месяца и дня (базовая)
    if not (1 <= month <= 12):
        print("Некорректная дата")
    elif not (1 <= day <= 31):
        print("Некорректная дата")
    else:
        # Определяем количество дней в месяце
        if month in [4, 6, 9, 11]:
            max_days = 30
        elif month == 2:
            # Проверка на високосность
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                max_days = 29
            else:
                max_days = 28
        else:
            max_days = 31
        
        # Финальная проверка
        if day <= max_days:
            print("Корректная дата")
        else:
            print("Некорректная дата")