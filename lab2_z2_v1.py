import math

def get_vertex_coordinates():
    """Ввод координат вершины с клавиатуры"""
    x = float(input("Введите координату x: "))
    y = float(input("Введите координату y: "))
    return x, y

def distance(x1, y1, x2, y2):
    """Расстояние между двумя точками"""
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx**2 + dy**2)

# Основная программа
print("Введите координаты вершин четырёхугольника M1, M2, M3, M4:")

vertices = []
for i in range(1, 5):
    print(f"\nВершина M{i}:")
    x, y = get_vertex_coordinates()
    vertices.append((x, y))

# Вычисление периметра
side_lengths = []
perimeter = 0

for i in range(4):
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i + 1) % 4]
    
    # Вычисляем длину стороны с промежуточными переменными
    dx = x2 - x1
    dy = y2 - y1
    side_length = math.sqrt(dx**2 + dy**2)
    
    side_lengths.append(side_length)
    perimeter += side_length

# Вывод результатов
print("\n" + "=" * 50)
print("РЕЗУЛЬТАТЫ:")
print("=" * 50)

for i, length in enumerate(side_lengths, 1):
    next_i = i + 1 if i < 4 else 1
    print(f"Сторона M{i}-M{next_i}: {length:.4f}")

print(f"\nПериметр четырёхугольника: {perimeter:.4f}")

# Вывод промежуточных переменных для первой стороны
print("\n" + "=" * 50)
print("ПРОМЕЖУТОЧНЫЕ ВЫЧИСЛЕНИЯ (для стороны M1-M2):")
print("=" * 50)
x1, y1 = vertices[0]
x2, y2 = vertices[1]
dx = x2 - x1
dy = y2 - y1
dx_squared = dx**2
dy_squared = dy**2
sum_squares = dx_squared + dy_squared
side_length = math.sqrt(sum_squares)

print(f"dx = {dx:.2f}")
print(f"dy = {dy:.2f}")
print(f"dx² = {dx_squared:.4f}")
print(f"dy² = {dy_squared:.4f}")
print(f"dx² + dy² = {sum_squares:.4f}")
print(f"√(dx² + dy²) = {side_length:.4f}")