from vehicle import Vehicle

class Bicycle(Vehicle):
    """
    Класс для велосипеда.
    Наследует базовый класс Vehicle.
    """
    
    def __init__(self, model="Unknown", speed=15, passengers=1, has_basket=False, gear_count=21):
        """
        Конструктор класса Bicycle.
        Вызывает конструктор родительского класса.
        
        Параметры:
            model (str): Название модели
            speed (float): Средняя скорость (км/ч)
            passengers (int): Число пассажиров
            has_basket (bool): Наличие корзины
            gear_count (int): Количество передач
        """
        # Вызов конструктора родительского класса
        super().__init__(model, speed, passengers)
        
        # Собственные поля
        self.has_basket = has_basket
        self.gear_count = gear_count
        print(f"[Bicycle] Добавлены детали велосипеда: корзина={has_basket}, передачи={gear_count}")
    
    def __del__(self):
        """Деструктор."""
        print(f"[Bicycle] Уничтожен велосипед '{self.model}'")
        # Вызов деструктора родителя
        super().__del__()
    
    def get_full_info(self):
        """
        Переопределение виртуального метода родителя.
        Возвращает полную информацию о велосипеде.
        """
        basket_info = "есть" if self.has_basket else "нет"
        return (f"Велосипед: {self.model}, "
                f"Скорость: {self.speed} км/ч, "
                f"Пассажиров: {self.passengers}, "
                f"Корзина: {basket_info}, "
                f"Передач: {self.gear_count}")
    
    def calculate_fuel_consumption(self, distance):
        """
        Переопределение метода родителя.
        Велосипед не потребляет топливо.
        """
        return 0
    
    def calculate_travel_time(self, distance):
        """
        Переопределение метода родителя с учётом особенностей велосипеда.
        """
        # Велосипед не может ехать бесконечно, скорость падает с усталостью
        if distance > 100:
            # На длинных дистанциях скорость снижается
            base_time = distance / self.speed
            fatigue_factor = 1 + (distance - 100) / 200  # доп. время на отдых
            return base_time * fatigue_factor
        return distance / self.speed