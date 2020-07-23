# https://stepik.org/lesson/3369/step/10?unit=952

"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен
сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
"""

# A = [['9', '5', '3'], ['0', '7', '-1'], ['-5', '2', '9']]
A = []
B = []
line = input()
while line != 'end':
    line = line.split()
    A.append(line)
    line = input()
# print(A)

for i in range(len(A) - 1):
    t_lst = []
    for j in range(len(A[i]) - 1):
        t = int(A[i - 1][j]) + int(A[i + 1][j]) + int(A[i][j - 1]) + int(A[i][j + 1])
        t_lst.append(t)
    j = len(A[i]) - 1
    t = int(A[i - 1][j]) + int(A[i + 1][j]) + int(A[i][j - 1]) + int(A[i][0])
    t_lst.append(t)
    B.append(t_lst)

i = len(A) - 1
t_lst = []
for j in range(len(A[i]) - 1):
    t = int(A[i - 1][j]) + int(A[0][j]) + int(A[i][j - 1]) + int(A[i][j + 1])
    t_lst.append(t)
j = len(A[i]) - 1
t = int(A[i - 1][j]) + int(A[0][j]) + int(A[i][j - 1]) + int(A[i][0])
t_lst.append(t)
B.append(t_lst)

for i in range(len(B)):
    for j in range(len(B[i])):
        print(B[i][j], end='\t')
    print()


# region Лучшее решение
"""
c = []
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c.append(a)
n, m = len(c), len(c[0])
for i in range(n):
    for j in range(m):
        x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
        print(x, end=' ')
    print()
"""
# endregion

