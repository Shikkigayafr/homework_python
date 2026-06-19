def input_matrix(rows, cols):
    """Ввод матрицы с клавиатуры"""
    matrix = []
    print(f"Введите матрицу {rows}x{cols}:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"M[{i}][{j}] = ")))
        matrix.append(row)
    return matrix

def print_matrix(matrix, title="Матрица"):
    """Вывод матрицы"""
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(f"{x:4d}" for x in row))

def find_max_min_indices(row):
    """Поиск индексов максимального и минимального элементов в строке"""
    max_idx = 0
    min_idx = 0
    for j in range(1, len(row)):
        if row[j] > row[max_idx]:
            max_idx = j
        if row[j] < row[min_idx]:
            min_idx = j
    return max_idx, min_idx

def swap_elements(row, max_idx, min_idx):
    """
    Замена максимального с первым, минимального с последним элементом
    Возвращает изменённую строку
    """
    row[0], row[max_idx] = row[max_idx], row[0]
    row[-1], row[min_idx] = row[min_idx], row[-1]
    return row

def process_matrix(matrix):
    """Обработка всех строк матрицы"""
    result = []
    for row in matrix:
        max_idx, min_idx = find_max_min_indices(row)
        new_row = swap_elements(row.copy(), max_idx, min_idx)
        result.append(new_row)
    return result

# Основная программа
def main():
    N = int(input("Введите количество строк N: "))
    M = int(input("Введите количество столбцов M: "))
    
    B = input_matrix(N, M)
    print_matrix(B, "Исходная матрица")
    
    result = process_matrix(B)
    print_matrix(result, "Матрица после замен")
    
    # Вывод деталей по строкам
    print("\n" + "=" * 60)
    print("ДЕТАЛИ ЗАМЕН:")
    print("=" * 60)
    for i in range(N):
        max_idx, min_idx = find_max_min_indices(B[i])
        print(f"Строка {i+1}:")
        print(f"  Макс = {B[i][max_idx]} (индекс {max_idx}) -> поменян с индексом 0")
        print(f"  Мин = {B[i][min_idx]} (индекс {min_idx}) -> поменян с индексом {M-1}")

if __name__ == "__main__":
    main()