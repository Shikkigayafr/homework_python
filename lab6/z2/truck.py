from vehicle import Vehicle

class Truck(Vehicle):
    """
    Класс для грузовика.
    Наследует базовый класс Vehicle.
    """
    
    def __init__(self, model="Unknown", speed=60, passengers=2, 
                 fuel_consumption=20, cargo_capacity=5000, has_awning=False):
        """
        Конструктор класса Truck.
        Вызывает конструктор родительского класса.
        
        Параметры:
            model (str): Название модели
            speed (float): Средняя скорость (км/ч)
            passengers (int): Число пассажиров
            fuel_consumption (float): Расход топлива (л/100 км)
            cargo_capacity (float): Грузоподъёмность (кг)
            has_awning (bool): Наличие тента
        """
        # Вызов конструктора родительского класса
        super().__init__(model, speed, passengers)
        
        # Собственные поля
        self.fuel_consumption = fuel_consumption
        self.cargo_capacity = cargo_capacity
        self.has_awning = has_awning
        print(f"[Truck] Добавлены детали грузовика: расход={fuel_consumption} л/100км, "
              f"грузоподъёмность={cargo_capacity}кг, тент={has_awning}")
    
    def __del__(self):
        """Деструктор."""
        print(f"[Truck] Уничтожен грузовик '{self.model}'")
        # Вызов деструктора родителя
        super().__del__()
    
    def get_full_info(self):
        """
        Переопределение виртуального метода родителя.
        Возвращает полную информацию о грузовике.
        """
        awning_info = "с тентом" if self.has_awning else "без тента"
        return (f"Грузовик: {self.model}, "
                f"Скорость: {self.speed} км/ч, "
                f"Пассажиров: {self.passengers}, "
                f"Расход: {self.fuel_consumption} л/100км, "
                f"Грузоподъёмность: {self.cargo_capacity} кг, "
                f"{awning_info}")
    
    def calculate_fuel_consumption(self, distance):
        """
        Переопределение метода родителя.
        Рассчитывает расход топлива с учётом загрузки грузовика.
        """
        # Базовый расход увеличивается на 10% при полной загрузке
        if self.cargo_capacity > 3000:
            factor = 1.1
        else:
            factor = 1.0
        
        return (self.fuel_consumption * distance * factor) / 100
    
    def calculate_travel_time(self, distance):
        """
        Переопределение метода родителя.
        Учитывает ограничения скорости для грузовиков.
        """
        # Грузовики медленнее на дорогах
        if distance > 500:
            # Дополнительное время на отдых для водителя
            rest_time = (distance // 500) * 0.75  # 45 минут на каждые 500 км
            return (distance / self.speed) + rest_time
        return distance / self.speed
    
    def get_fuel_info(self, distance):
        """
        Переопределение метода родителя.
        Возвращает информацию о топливе для грузовика.
        """
        fuel = self.calculate_fuel_consumption(distance)
        return f"Расход топлива: {fuel:.2f} л (с учётом загрузки)"