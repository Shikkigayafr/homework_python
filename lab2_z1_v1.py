import math
from decimal import Decimal, getcontext

# Установка высокой точности для Decimal (50 знаков)
getcontext().prec = 50

def calculate_with_float(n_val):
    """Вычисление с использованием типа float (двойная точность)"""
    phi = math.pi / 4
    phi_float = float(phi)
    n_float = float(n_val)
    
    # Промежуточные переменные
    a = math.tan(phi_float * n_float)
    print(f"  a (float) = {a}")
    
    # Вычисление первого слагаемого: 5a^(-2)
    term1 = 5 * (a ** -2)
    print(f"  term1 (float) = {term1}")
    
    # Вычисление второго слагаемого: |tg(pi*n/(2*phi))| * sqrt(e^(5a))
    angle = (math.pi * n_float) / (2 * phi_float)
    tg_value = math.tan(angle)
    abs_tg = abs(tg_value)
    print(f"  |tg| (float) = {abs_tg}")
    
    exp_val = math.exp(5 * a)
    sqrt_exp = math.sqrt(exp_val)
    print(f"  sqrt(e^(5a)) (float) = {sqrt_exp}")
    
    term2 = abs_tg * sqrt_exp
    print(f"  term2 (float) = {term2}")
    
    result = term1 - term2
    return result

def calculate_with_decimal(n_val):
    """Вычисление с использованием Decimal для высокой точности"""
    # Константы как Decimal
    pi = Decimal(str(math.pi))
    phi = pi / Decimal(4)
    n = Decimal(str(n_val))
    phi_n = phi * n
    
    # a = tg(phi * n) — вычисляем через float, потом конвертируем (для простоты)
    # В реальности Decimal не имеет встроенной функции tan
    a_float = math.tan(float(phi_n))
    a = Decimal(str(a_float))
    print(f"  a (Decimal) = {a}")
    
    # term1 = 5 * a^(-2)
    term1 = Decimal(5) * (a ** Decimal(-2))
    print(f"  term1 (Decimal) = {term1}")
    
    # term2 = |tg(pi*n/(2*phi))| * sqrt(e^(5a))
    angle = (pi * n) / (Decimal(2) * phi)
    tg_float = math.tan(float(angle))
    abs_tg = Decimal(str(abs(tg_float)))
    print(f"  |tg| (Decimal) = {abs_tg}")
    
    exp_val = (Decimal(5) * a).exp()
    sqrt_exp = exp_val.sqrt()
    print(f"  sqrt(e^(5a)) (Decimal) = {sqrt_exp}")
    
    term2 = abs_tg * sqrt_exp
    print(f"  term2 (Decimal) = {term2}")
    
    result = term1 - term2
    return result

# Основная часть программы
if __name__ == "__main__":
    print("=" * 60)
    print("ВЫЧИСЛЕНИЕ ЗНАЧЕНИЯ ВЫРАЖЕНИЯ")
    print("=" * 60)
    
    n = 6  # целое значение
    
    print("\n1. Вычисление с типом float (стандартная двойная точность):")
    print("-" * 50)
    result_float = calculate_with_float(n)
    print(f"\n  РЕЗУЛЬТАТ (float): {result_float}")
    
    print("\n2. Вычисление с типом Decimal (высокая точность):")
    print("-" * 50)
    result_decimal = calculate_with_decimal(n)
    print(f"\n  РЕЗУЛЬТАТ (Decimal): {result_decimal}")
    
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ РЕЗУЛЬТАТОВ:")
    print(f"  float:   {result_float}")
    print(f"  Decimal: {result_decimal}")
    print(f"  Разница: {abs(result_float - float(result_decimal))}")
    print("=" * 60)