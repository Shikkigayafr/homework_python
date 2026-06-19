import math

def circle_area():
    """Вычисление площади круга"""
    radius = float(input("Введите радиус круга: "))
    area = math.pi * radius ** 2
    print(f"Площадь круга: {area:.2f}")
    return area

def rectangle_area():
    """Вычисление площади прямоугольника"""
    width = float(input("Введите ширину прямоугольника: "))
    height = float(input("Введите высоту прямоугольника: "))
    area = width * height
    print(f"Площадь прямоугольника: {area:.2f}")
    return area

def triangle_area():
    """Вычисление площади треугольника (по основанию и высоте)"""
    base = float(input("Введите длину основания треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    area = 0.5 * base * height
    print(f"Площадь треугольника: {area:.2f}")
    return area

def triangle_heron_area():
    """Вычисление площади треугольника по трём сторонам (формула Герона)"""
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    
    # Проверка существования треугольника
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2  # полупериметр
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"Площадь треугольника (по формуле Герона): {area:.2f}")
        return area
    else:
        print("Ошибка: Треугольник с такими сторонами не существует!")
        return None

def trapezoid_area():
    """Вычисление площади трапеции"""
    a = float(input("Введите длину первого основания: "))
    b = float(input("Введите длину второго основания: "))
    h = float(input("Введите высоту трапеции: "))
    area = (a + b) / 2 * h
    print(f"Площадь трапеции: {area:.2f}")
    return area

def parallelogram_area():
    """Вычисление площади параллелограмма"""
    base = float(input("Введите длину основания: "))
    height = float(input("Введите высоту параллелограмма: "))
    area = base * height
    print(f"Площадь параллелограмма: {area:.2f}")
    return area

def rhombus_area():
    """Вычисление площади ромба (по диагоналям)"""
    d1 = float(input("Введите длину первой диагонали: "))
    d2 = float(input("Введите длину второй диагонали: "))
    area = (d1 * d2) / 2
    print(f"Площадь ромба: {area:.2f}")
    return area

def square_area():
    """Вычисление площади квадрата"""
    side = float(input("Введите длину стороны квадрата: "))
    area = side ** 2
    print(f"Площадь квадрата: {area:.2f}")
    return area

def ellipse_area():
    """Вычисление площади эллипса"""
    a = float(input("Введите большую полуось: "))
    b = float(input("Введите малую полуось: "))
    area = math.pi * a * b
    print(f"Площадь эллипса: {area:.2f}")
    return area

def main():
    """Главное меню программы"""
    while True:
        print("\n" + "=" * 50)
        print("ВЫЧИСЛЕНИЕ ПЛОЩАДИ ГЕОМЕТРИЧЕСКИХ ФИГУР")
        print("=" * 50)
        print("Выберите фигуру:")
        print("  1. Круг")
        print("  2. Прямоугольник")
        print("  3. Треугольник (по основанию и высоте)")
        print("  4. Треугольник (по трём сторонам, формула Герона)")
        print("  5. Трапеция")
        print("  6. Параллелограмм")
        print("  7. Ромб (по диагоналям)")
        print("  8. Квадрат")
        print("  9. Эллипс")
        print("  0. Выход")
        print("-" * 50)
        
        choice = input("Ваш выбор: ")
        
        if choice == '1':
            circle_area()
        elif choice == '2':
            rectangle_area()
        elif choice == '3':
            triangle_area()
        elif choice == '4':
            triangle_heron_area()
        elif choice == '5':
            trapezoid_area()
        elif choice == '6':
            parallelogram_area()
        elif choice == '7':
            rhombus_area()
        elif choice == '8':
            square_area()
        elif choice == '9':
            ellipse_area()
        elif choice == '0':
            print("Программа завершена. До свидания!")
            break
        else:
            print("Ошибка: Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()