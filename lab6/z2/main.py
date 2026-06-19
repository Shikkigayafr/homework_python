from vehicle import Vehicle
from bicycle import Bicycle
from car import Car
from truck import Truck

def print_header(text):
    """Вывод заголовка с разделителями."""
    print("\n" + "=" * 70)
    print(text)
    print("=" * 70)

def print_separator():
    """Вывод разделителя."""
    print("-" * 70)

def demonstrate_vehicle_creation():
    """Демонстрация создания объектов всех классов."""
    print_header("1. ДЕМОНСТРАЦИЯ СОЗДАНИЯ ОБЪЕКТОВ")
    
    # Базовый класс
    print("\nСоздание Vehicle (базовый класс):")
    vehicle = Vehicle("Самокат", 12, 1)
    print(f"  Информация: {vehicle.get_info()}")
    
    # Велосипед
    print("\nСоздание Bicycle (наследник):")
    bike = Bicycle("GT Avalanche", 22, 1, True, 27)
    print(f"  Информация: {bike.get_info()}")
    print(f"  Полная информация: {bike.get_full_info()}")
    
    # Автомобиль
    print("\nСоздание Car (наследник):")
    car = Car("Toyota Camry", 95, 4, 8.5, True)
    print(f"  Информация: {car.get_info()}")
    print(f"  Полная информация: {car.get_full_info()}")
    
    # Грузовик
    print("\nСоздание Truck (наследник):")
    truck = Truck("Kamaz 6520", 70, 2, 25, 8000, True)
    print(f"  Информация: {truck.get_info()}")
    print(f"  Полная информация: {truck.get_full_info()}")
    
    return vehicle, bike, car, truck

def demonstrate_vehicle_methods(objects):
    """Демонстрация работы методов всех классов."""
    print_header("2. ДЕМОНСТРАЦИЯ РАБОТЫ МЕТОДОВ")
    
    distance = 150  # км
    print(f"Расстояние: {distance} км")
    print_separator()
    
    vehicle, bike, car, truck = objects
    
    # Демонстрация для каждого объекта
    for name, obj in [
        ("Vehicle (базовый)", vehicle),
        ("Bicycle (велосипед)", bike),
        ("Car (автомобиль)", car),
        ("Truck (грузовик)", truck)
    ]:
        print(f"\n{name}:")
        print(f"  Модель: {obj.model}")
        print(f"  Скорость: {obj.speed} км/ч")
        print(f"  Время на {distance} км: {obj.calculate_travel_time(distance):.2f} ч")
        print(f"  {obj.get_fuel_info(distance)}")
        print(f"  Полная информация: {obj.get_full_info()}")

def demonstrate_polymorphism():
    """Демонстрация полиморфизма - вызов методов через базовый класс."""
    print_header("3. ДЕМОНСТРАЦИЯ ПОЛИМОРФИЗМА")
    
    distance = 200
    print(f"Расстояние: {distance} км")
    print_separator()
    
    # Список объектов в виде базового класса
    vehicles = [
        Vehicle("Общий транспорт", 50, 2),
        Bicycle("GT Avalanche", 22, 1, True, 27),
        Car("Toyota Camry", 95, 4, 8.5, True),
        Truck("Kamaz 6520", 70, 2, 25, 8000, True)
    ]
    
    for obj in vehicles:
        print(f"\nТип: {obj.__class__.__name__}")
        print(f"  {obj.get_info()}")
        print(f"  Время в пути ({distance} км): {obj.calculate_travel_time(distance):.2f} ч")
        print(f"  Расход топлива: {obj.calculate_fuel_consumption(distance):.2f} л")
        print(f"  Полная информация: {obj.get_full_info()}")

def demonstrate_inheritance_chain():
    """Демонстрация вызова конструкторов родительских классов."""
    print_header("4. ДЕМОНСТРАЦИЯ НАСЛЕДОВАНИЯ")
    
    print("\nСоздание объекта Car с вызовом всех конструкторов:")
    print_separator()
    car = Car("BMW X5", 110, 5, 12, True)
    
    print("\nСоздание объекта Truck с вызовом всех конструкторов:")
    print_separator()
    truck = Truck("Volvo FH", 85, 2, 30, 12000, False)
    
    return car, truck

def interactive_mode():
    """Интерактивный режим - пользователь выбирает тип объекта."""
    print_header("5. ИНТЕРАКТИВНЫЙ РЕЖИМ")
    
    while True:
        print("\nВыберите тип объекта для демонстрации:")
        print("  1. Vehicle (базовый)")
        print("  2. Bicycle (велосипед)")
        print("  3. Car (автомобиль)")
        print("  4. Truck (грузовик)")
        print("  5. Сравнить все типы")
        print("  0. Выйти в главное меню")
        print("-" * 70)
        
        choice = input("Ваш выбор: ")
        
        distance = float(input("Введите расстояние (км): "))
        
        if choice == '1':
            model = input("Модель: ")
            speed = float(input("Скорость (км/ч): "))
            passengers = int(input("Количество пассажиров: "))
            obj = Vehicle(model, speed, passengers)
            
        elif choice == '2':
            model = input("Модель: ")
            speed = float(input("Скорость (км/ч): "))
            passengers = int(input("Количество пассажиров: "))
            basket = input("Наличие корзины (да/нет): ").lower() == 'да'
            gears = int(input("Количество передач: "))
            obj = Bicycle(model, speed, passengers, basket, gears)
            
        elif choice == '3':
            model = input("Модель: ")
            speed = float(input("Скорость (км/ч): "))
            passengers = int(input("Количество пассажиров: "))
            fuel = float(input("Расход топлива (л/100км): "))
            automatic = input("АКПП (да/нет): ").lower() == 'да'
            obj = Car(model, speed, passengers, fuel, automatic)
            
        elif choice == '4':
            model = input("Модель: ")
            speed = float(input("Скорость (км/ч): "))
            passengers = int(input("Количество пассажиров: "))
            fuel = float(input("Расход топлива (л/100км): "))
            cargo = float(input("Грузоподъёмность (кг): "))
            awning = input("Наличие тента (да/нет): ").lower() == 'да'
            obj = Truck(model, speed, passengers, fuel, cargo, awning)
            
        elif choice == '5':
            compare_all_types(distance)
            continue
            
        elif choice == '0':
            break
            
        else:
            print("Неверный выбор!")
            continue
        
        print("\n" + "=" * 70)
        print("РЕЗУЛЬТАТЫ ДЕМОНСТРАЦИИ:")
        print("=" * 70)
        print(f"Тип объекта: {obj.__class__.__name__}")
        print(f"Информация: {obj.get_info()}")
        print(f"Полная информация: {obj.get_full_info()}")
        print(f"Время на {distance} км: {obj.calculate_travel_time(distance):.2f} ч")
        print(f"Расход топлива на {distance} км: {obj.calculate_fuel_consumption(distance):.2f} л")
        print("=" * 70)

def compare_all_types(distance):
    """Сравнение всех типов транспортных средств."""
    print(f"\nСРАВНЕНИЕ ВСЕХ ТИПОВ (расстояние: {distance} км):")
    print_separator()
    
    objects = [
        Vehicle("Самокат", 15, 1),
        Bicycle("GT Avalanche", 22, 1, True, 27),
        Car("Toyota Camry", 95, 4, 8.5, True),
        Truck("Kamaz 6520", 70, 2, 25, 8000, True)
    ]
    
    print(f"{'Тип':<15} {'Модель':<20} {'Время (ч)':<12} {'Топливо (л)':<12} {'Пассажиры':<10}")
    print_separator()
    
    for obj in objects:
        time = obj.calculate_travel_time(distance)
        fuel = obj.calculate_fuel_consumption(distance)
        print(f"{obj.__class__.__name__:<15} "
              f"{obj.model[:18]:<20} "
              f"{time:<12.2f} "
              f"{fuel:<12.2f} "
              f"{obj.passengers:<10}")

def main():
    """Главная функция программы."""
    print_header("ЛАБОРАТОРНАЯ РАБОТА №6")
    print("Иерархия классов: Vehicle (средство передвижения)")
    print("Наследники: Bicycle, Car, Truck")
    print("=" * 70)
    
    # Создание объектов для демонстрации
    vehicle, bike, car, truck = demonstrate_vehicle_creation()
    objects = (vehicle, bike, car, truck)
    
    while True:
        print("\n" + "=" * 70)
        print("ГЛАВНОЕ МЕНЮ:")
        print("=" * 70)
        print("  1. Демонстрация создания объектов")
        print("  2. Демонстрация работы методов")
        print("  3. Демонстрация полиморфизма")
        print("  4. Демонстрация наследования (вызов конструкторов)")
        print("  5. Интерактивный режим (выбор пользователя)")
        print("  0. Выход")
        print("-" * 70)
        
        choice = input("Ваш выбор: ")
        
        if choice == '1':
            demonstrate_vehicle_creation()
        elif choice == '2':
            demonstrate_vehicle_methods(objects)
        elif choice == '3':
            demonstrate_polymorphism()
        elif choice == '4':
            demonstrate_inheritance_chain()
        elif choice == '5':
            interactive_mode()
        elif choice == '0':
            print("\nПрограмма завершена. До свидания!")
            break
        else:
            print("Ошибка: неверный выбор!")

if __name__ == "__main__":
    main()