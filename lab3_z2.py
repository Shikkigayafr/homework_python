def is_in_square(x, y):
   
    return -4 <= x <= 0 and 3 <= y <= 5

def is_in_triangle(x, y):
    """Треугольник: x ∈ [-4, 0], y ∈ [5, 8]"""
    if not (-4 <= x <= 0 and 5 <= y <= 8):
        return False
    y_line = 5 + (3/4) * (x + 4)  # линия от (-4,5) до (0,8)
    return y <= y_line

def is_in_area(x, y):
    """Область: квадрат + треугольник (без промежутка)"""
    return is_in_square(x, y) or is_in_triangle(x, y)

# Ввод данных
x = float(input("Введите X: "))
y = float(input("Введите Y: "))

if is_in_area(x, y):
    print(f"Точка ({x}, {y}) ВНУТРИ области")
else:
    print(f"Точка ({x}, {y}) ВНЕ области")