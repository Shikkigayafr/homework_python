from vehicle import Vehicle

class Car(Vehicle):
    """
    Класс для легкового автомобиля.
    Наследует базовый класс Vehicle.
    """
    
    def __init__(self, model="Unknown", speed=80, passengers=4, fuel_consumption=8, is_automatic=True):
        """
        Конструктор класса Car.
        Вызывает конструктор родительского класса.
        
        Параметры:
            model (str): Название модели
            speed (float): Средняя скорость (км/ч)
            passengers (int): Число пассажиров
            fuel_consumption (float): Расход топлива (л/100 км)
            is_automatic (bool): Автоматическая коробка передач
        """
        # Вызов конструктора родительского класса
        super().__init__(model, speed, passengers)
        
        # Собственные поля
        self.fuel_consumption = fuel_consumption
        self.is_automatic = is_automatic
        print(f"[Car] Добавлены детали авто: расход={fuel_consumption} л/100км, АКПП={is_automatic}")
    
    def __del__(self):
        """Деструктор."""
        print(f"[Car] Уничтожен автомобиль '{self.model}'")
        # Вызов деструктора родителя
        super().__del__()
    
    def get_full_info(self):
        """
        Переопределение виртуального метода родителя.
        Возвращает полную информацию об автомобиле.
        """
        gearbox = "АКПП" if self.is_automatic else "МКПП"
        return (f"Автомобиль: {self.model}, "
                f"Скорость: {self.speed} км/ч, "
                f"Пассажиров: {self.passengers}, "
                f"Расход: {self.fuel_consumption} л/100км, "
                f"КПП: {gearbox}")
    
    def calculate_fuel_consumption(self, distance):
        """
        Переопределение метода родителя.
        Рассчитывает расход топлива для заданного расстояния.
        """
        return (self.fuel_consumption * distance) / 100
    
    def calculate_travel_time(self, distance):
        """
        Переопределение метода родителя.
        Учитывает возможные остановки на заправку.
        """
        base_time = distance / self.speed
        
        # Добавляем время на заправку, если дистанция большая
        fuel_needed = self.calculate_fuel_consumption(distance)
        fuel_tank_capacity = 50  # литров
        stops = fuel_needed // fuel_tank_capacity
        refuel_time = stops * 0.25  # 15 минут на заправку
        
        return base_time + refuel_time
    
    def get_fuel_info(self, distance):
        """
        Переопределение метода родителя.
        Возвращает информацию о топливе для автомобиля.
        """
        fuel = self.calculate_fuel_consumption(distance)
        return f"Расход топлива: {fuel:.2f} л (на {distance} км)"