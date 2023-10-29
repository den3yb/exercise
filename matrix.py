from multiprocessing import pool
from time import sleep

s = int(input("Ввеедите количество рядов"))  
c = int(input("Введите количество столбцов"))  
matrix = []
for i in range (s):
    m=[]
    for j in range (c):
        m.append(int(input()))
    matrix.append(m)

for i in range (s):
    for j in range (c):
        print(matrix[i][j], end = " ")
    print()

