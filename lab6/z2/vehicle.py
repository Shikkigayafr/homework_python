class Vehicle:
    """
    Базовый класс для всех средств передвижения.
    Содержит общие поля и методы для всех транспортных средств.
    """
    
    def __init__(self, model="Unknown", speed=0, passengers=1):
        """
        Конструктор базового класса.
        
        Параметры:
            model (str): Название модели
            speed (float): Средняя скорость (км/ч)
            passengers (int): Число пассажиров
        """
        self.model = model
        self.speed = speed
        self.passengers = passengers
        print(f"[Vehicle] Создан объект модели '{model}'")
    
    def __del__(self):
        """Деструктор."""
        print(f"[Vehicle] Уничтожен объект модели '{self.model}'")
    
    def get_info(self):
        """
        Возвращает строку с основной информацией о средстве передвижения.
        """
        return (f"Модель: {self.model}, "
                f"Средняя скорость: {self.speed} км/ч, "
                f"Пассажиров: {self.passengers}")
    
    def get_full_info(self):
        """
        Возвращает полную информацию о средстве передвижения.
        Виртуальный метод, который будет переопределён в наследниках.
        """
        return self.get_info()
    
    def calculate_fuel_consumption(self, distance):
        """
        Рассчитывает потребление топлива для заданного расстояния.
        
        Параметры:
            distance (float): Расстояние в километрах
            
        Возвращает:
            float: Расход топлива в литрах (для транспорта без двигателя - 0)
        """
        # Базовый метод для транспорта без двигателя
        return 0
    
    def calculate_travel_time(self, distance):
        """
        Вычисляет время движения на заданное расстояние.
        
        Параметры:
            distance (float): Расстояние в километрах
            
        Возвращает:
            float: Время в часах
        """
        if self.speed <= 0:
            return float('inf')
        return distance / self.speed
    
    def get_fuel_info(self, distance):
        """
        Возвращает строку с информацией о топливе.
        """
        fuel = self.calculate_fuel_consumption(distance)
        if fuel == 0:
            return "Не требует топлива"
        return f"Расход топлива: {fuel:.2f} л"