# Формируется матрица F следующим образом: если в Е количество чисел, больших К в четных столбцах в области 1 больше, чем произведение чисел в нечетных строках в области 4,
# то поменять в Е симметрично области 2 и 3 местами, иначе С и В поменять местами несимметрично. При этом матрица А не меняется.
# После чего вычисляется выражение: (К*(A*F))* Fт. Выводятся по мере формирования А, F и все матричные операции последовательно.
import random

K_test = 3 # Тестовые данные
N_test = 10
E_test = [
    [9, 5, 1, 6, -3],
    [1, 6, -5, -1, -4],
    [-8, -2, -3, 7, 9],
    [-7, 6, 0, -8, 4],
    [-3, -9, -4, -1, -5]]
B_test = [
    [-8, -7, 1, 1, 10],
    [-1, 10, 5, -10, -6],
    [1, 8, 0, 9, 5],
    [2, 1, -8, -5, -1],
    [-3, -6, 9, 7, -6]]
C_test = [
    [5, 7, -1, -7, -6],
    [2, 3, 10, -8, 4],
    [-4, -7, -10, 15, 5],
    [0, 9, -8, 9, 4],
    [10, -8, -10, -1, 8]]
D_test = [
    [-7, 1, 7, 8, -3],
    [-1, 6, -5, 2, 2],
    [-4, -2, 1, -2, -2],
    [2, -3, 0, -7, -1],
    [-8, -10, 3, 0, -5]]

print('Использовать тестовые данные или случайные?')
while True:
    choice = input('Введите 1, если хотите использовать тестовые данные, 2 - если случайные, q - для выхода из программы): ')
    if choice == '1' or choice == '2' or choice == 'q':
        break

if choice == '1':
    K = K_test
    N = N_test
    B, C, D, E = B_test, C_test, D_test, E_test
    n = N // 2  # Размерность матриц B, C, D, E (n x n)

if choice == '2': # Генерация случайных данных
    K = int(input("Введите число К = "))
    while True:
        N = int(input("Введите число N = "))
        if N < 6:
            print('Число N слишком малое. Введите N >= 6')
        else:
            break
    B, C, D, E = [], [], [], []
    n = N // 2  # Размерность матриц B, C, D, E (n x n)
    for row in range(n):
        row_b, row_c, row_d, row_e = [], [], [], []
        for col in range(n):
            row_b.append(random.randint(-10, 10))
            row_c.append(random.randint(-10, 10))
            row_d.append(random.randint(-10, 10))
            row_e.append(random.randint(-10, 10))
        B.append(row_b)
        C.append(row_c)
        D.append(row_d)
        E.append(row_e)

if choice == 'q':
    exit()

if N % 2 == 0:
    print("Число N чётное, в итоговой матрице А будут обрабатываться все элементы")
else:
    print(f'Число N нечётное, в итоговой матрице А не будут обрабатываться элементы {N//2+1} строки и столбца, т.к. они не входят в подматрицы')

A = []
for row in range(n):
    A.insert(row, E[row] + B[row])
    A.insert(row+5, D[row] + C[row])

# Печатаем матрицы E, B, C, D, A
print('Матрица E:')
for row in range(n):
    print(E[row])

print('Матрица B:')
for row in range(n):
    print(B[row])

print('Матрица C:')
for row in range(n):
    print(C[row])

print('Матрица D:')
for row in range(n):
    print(D[row])

print('Матрица A:')
for row in range(len(A)):
    print(A[row])

# Считаем произведение чисел в нечетных строках в области 4 в матрице E
x = 1
for row in range (1, n//2+1):
    for col in range(row, n-row):
        if col % 2 == 0: # Нумерация строк начинается с 1
            x *= E[col][row-1]
print(f'Произведение чисел в нечетных строках в области 4 в матрице E: {x}')

# Считаем количество чисел, больших К в четных столбцах в области 1 в матрице E
count_more_K = 0
for row in range(1, n//2+1):
    for col in range(row, n-row):
        if col % 2 == 1:  # Нумерация столбцов начинается с 1
            if E[col][row*-1] > K:
                count_more_K += 1  # Увеличиваем счетчик
print(f'Количество чисел, больших К в четных столбцах в области 1 в матрице E: {count_more_K}')

F = [] # Создаём матрицу F следующим образом
if count_more_K > x: # Если выполняется условие
    E_F = E
    for row in range (1, n//2+1):
        for col in range(row, n-row):
            E_F[row-1][col], E_F[col][row-1] = E_F[col][row-1], E_F[row-1][col]
    print('Матрица E_F')
    for row in range(n):
        F.insert(row, E_F[row] + B[row])
        F.insert(row+5, D[row] + C[row])
else: # иначе С и В поменять местами несимметрично
    for row in range(n):
        F.insert(row, E[row] + B[row])
        F.insert(row+5, D[row] + C[row])
print('Матрица F:')
for row in range(len(F)):
    print(F[row])
    
# К*(A*F)*Fт

A_and_F = []  # Умножаем матрицы A и F
for row in range(len(A)):
    F_row = []
    for i in range(len(A)):
        sum = 0
        for j in range(len(A)):
            sum += A[row][j] * F[j][i]
        F_row.append(sum)
    A_and_F.append(F_row)

print('Матрица A*F:')
for row in range(len(A)):
    print(A_and_F[row])

A_and_F_and_K = [] # Умножаем произведение матриц A и F на константу K
for row in range(len(A)):
    cur_row = []
    for col in range(len(A)):
        cur_row.append(0)
    A_and_F_and_K.append(cur_row)  # формируем пустую матрицу, чтобы была возможность доступа к элементам матрицы по индексам

for row in range(len(A)):
    for col in range(len(A)):
        A_and_F_and_K[row][col] = K * A_and_F[row][col]

print('Матрица F*A*K:')
for row in range(len(A)):
    print(A_and_F_and_K[row])

F_transpose = [] # Транспонируем матрицу F
for row in range(len(F)):
    F_transpose_row = []
    for col in range(len(F)):
        F_transpose_row.append(F[col][row])
    F_transpose.append(F_transpose_row)

print('Транспонированная матрица F:')
for row in range(len(F)):
    print(F_transpose[row])

result = []  # Результат(произведение A*F*K и Fт)
for row in range(len(A)):  # Формируем пустую матрицу, чтобы была возможность доступа к элементам матрицы по индексам
    cur_row = []
    for col in range(len(A)):
        cur_row.append(0)
    result.append(cur_row)

for row in range(len(A)):
    for col in range(len(A)):
        result[row][col] = A_and_F_and_K[row][col] * F[row][col]

print('Результат:')
for row in range(len(A)):
    print(result[row])
