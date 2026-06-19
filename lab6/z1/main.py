from date_class import Date

def print_header(text):
    """Вывод заголовка с разделителями"""
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)

def demonstrate_constructors():
    """Демонстрация работы конструкторов"""
    print_header("ДЕМОНСТРАЦИЯ КОНСТРУКТОРОВ")
    
    # 1. Конструктор по умолчанию
    print("\n1. Создание объекта с конструктором по умолчанию:")
    date1 = Date()
    print(f"   Объект: {date1.get_info()}")
    
    # 2. Создание с заданными значениями (константами)
    print("\n2. Создание объекта с константными значениями:")
    date2 = Date(15, 8, 2024)
    print(f"   Объект: {date2.get_info()}")
    
    return date1, date2

def demonstrate_methods():
    """Демонстрация работы методов класса"""
    print_header("ДЕМОНСТРАЦИЯ МЕТОДОВ")
    
    # Создание объекта для демонстрации
    date = Date(28, 2, 2024)
    print(f"\nИсходная дата: {date.get_info()}")
    
    # Метод 1: Проверка на високосность
    print("\n1. Проверка на високосность:")
    if date.is_leap_year():
        print(f"   Год {date.year} - високосный")
    else:
        print(f"   Год {date.year} - не високосный")
    
    # Метод 2: Увеличение даты на 5 дней
    print(f"\n2. Увеличение даты на 5 дней:")
    date.add_days(5)
    print(f"   Дата после увеличения: {date.get_info()}")
    
    # Дополнительная информация
    print("\n3. Расширенная информация об объекте:")
    print(f"   {date.get_full_info()}")

def demonstrate_user_input():
    """Демонстрация создания объекта с вводом от пользователя"""
    print_header("СОЗДАНИЕ ОБЪЕКТА С ВВОДОМ ОТ ПОЛЬЗОВАТЕЛЯ")
    
    print("\nВведите данные для создания объекта Date:")
    
    while True:
        try:
            day = int(input("  Введите день (1-31): "))
            month = int(input("  Введите месяц (1-12): "))
            year = int(input("  Введите год: "))
            
            # Простая валидация
            if 1 <= day <= 31 and 1 <= month <= 12:
                break
            else:
                print("  Ошибка: некорректные значения! Попробуйте снова.")
        except ValueError:
            print("  Ошибка: введите целые числа!")
    
    # Создание объекта с введёнными значениями
    user_date = Date(day, month, year)
    print(f"\nСоздан объект: {user_date.get_info()}")
    
    # Демонстрация работы методов
    print(f"\nПроверка года {user_date.year}:")
    if user_date.is_leap_year():
        print("  Год високосный")
    else:
        print("  Год не високосный")
    
    print(f"\nУвеличение даты на 5 дней:")
    user_date.add_days(5)
    print(f"  Дата после увеличения: {user_date.get_info()}")

def demonstrate_three_objects():
    """Создание трёх объектов и вывод результатов"""
    print_header("СОЗДАНИЕ ТРЁХ ОБЪЕКТОВ")
    
    # Объект 1: конструктор по умолчанию
    print("\n1. Объект с конструктором по умолчанию:")
    obj1 = Date()
    print(f"   Дата: {obj1.get_info()}")
    print(f"   Информация: {obj1.get_full_info()}")
    
    # Объект 2: с константными значениями
    print("\n2. Объект с константными значениями (31.12.2024):")
    obj2 = Date(31, 12, 2024)
    print(f"   Дата: {obj2.get_info()}")
    print(f"   Информация: {obj2.get_full_info()}")
    
    # Объект 3: с введёнными значениями
    print("\n3. Объект с введёнными значениями:")
    try:
        day = int(input("  Введите день: "))
        month = int(input("  Введите месяц: "))
        year = int(input("  Введите год: "))
        obj3 = Date(day, month, year)
        print(f"   Дата: {obj3.get_info()}")
        print(f"   Информация: {obj3.get_full_info()}")
    except ValueError:
        print("  Ошибка ввода! Создан объект с значениями по умолчанию.")
        obj3 = Date()
    
    # Демонстрация работы методов для всех объектов
    print("\n" + "-" * 60)
    print("РЕЗУЛЬТАТЫ РАБОТЫ МЕТОДОВ ДЛЯ ВСЕХ ОБЪЕКТОВ:")
    print("-" * 60)
    
    objects = [obj1, obj2, obj3]
    for i, obj in enumerate(objects, 1):
        print(f"\nОбъект {i}: {obj.get_info()}")
        print(f"  Високосный: {'Да' if obj.is_leap_year() else 'Нет'}")
        # Увеличиваем на 5 дней
        obj_copy = Date(obj.day, obj.month, obj.year)  # Копия для сохранения
        obj_copy.add_days(5)
        print(f"  +5 дней: {obj_copy.get_info()}")
        # Расширенная информация
        print(f"  Полная информация: {obj.get_full_info()}")

def main():
    """Основная функция программы"""
    print_header("ЛАБОРАТОРНАЯ РАБОТА №1")
    print("Класс: Date (Дата)")
    print("Поля: день, месяц, год")
    print("=" * 60)
    
    while True:
        print("\nМЕНЮ:")
        print("  1. Демонстрация конструкторов")
        print("  2. Демонстрация методов класса")
        print("  3. Создание объекта с вводом от пользователя")
        print("  4. Создание трёх объектов")
        print("  5. Полная демонстрация (все пункты)")
        print("  0. Выход")
        print("-" * 60)
        
        choice = input("Ваш выбор: ")
        
        if choice == '1':
            demonstrate_constructors()
        elif choice == '2':
            demonstrate_methods()
        elif choice == '3':
            demonstrate_user_input()
        elif choice == '4':
            demonstrate_three_objects()
        elif choice == '5':
            demonstrate_constructors()
            demonstrate_methods()
            demonstrate_user_input()
            demonstrate_three_objects()
        elif choice == '0':
            print("\nПрограмма завершена. До свидания!")
            break
        else:
            print("Ошибка: неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()