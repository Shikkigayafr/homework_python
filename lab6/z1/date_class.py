class Date:
    """
    Класс для работы с датами.
    Поля: день, месяц, год.
    """
    
    def __init__(self, day=1, month=1, year=2000):
        """
        Конструктор по умолчанию.
        Если параметры не указаны, устанавливает дату: 01.01.2000
        """
        self.day = day
        self.month = month
        self.year = year
        print(f"Создан объект Date: {self.get_info()}")
    
    def __del__(self):
        """
        Деструктор. Освобождает память (в Python вызывается сборщиком мусора).
        """
        print(f"Уничтожен объект Date: {self.get_info()}")
    
    def is_leap_year(self):
        """
        Функция-метод 1: Определяет, является ли год високосным.
        Возвращает True, если год високосный, иначе False.
        """
        year = self.year
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            return True
        return False
    
    def get_days_in_month(self):
        """
        Вспомогательный метод: возвращает количество дней в месяце.
        """
        if self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28
        else:
            return 31
    
    def add_days(self, days=5):
        """
        Функция-метод 2: Увеличивает дату на указанное количество дней (по умолчанию на 5).
        Возвращает новую дату (изменяет текущий объект).
        """
        remaining_days = days
        while remaining_days > 0:
            days_in_month = self.get_days_in_month()
            
            # Если добавить можно без перехода на следующий месяц
            if self.day + remaining_days <= days_in_month:
                self.day += remaining_days
                remaining_days = 0
            else:
                # Переходим на следующий месяц
                remaining_days -= (days_in_month - self.day + 1)
                self.day = 1
                self.month += 1
                
                # Если перешли на следующий год
                if self.month > 12:
                    self.month = 1
                    self.year += 1
        
        return self
    
    def get_info(self):
        """
        Функция формирования строки информации об объекте.
        Возвращает строку с датой в формате ДД.ММ.ГГГГ.
        """
        return f"{self.day:02d}.{self.month:02d}.{self.year:04d}"
    
    def get_full_info(self):
        """
        Дополнительный метод: возвращает расширенную информацию об объекте.
        """
        leap_status = "високосный" if self.is_leap_year() else "не високосный"
        days_in_month = self.get_days_in_month()
        return (f"Дата: {self.get_info()}, "
                f"Год {leap_status}, "
                f"Дней в месяце: {days_in_month}")