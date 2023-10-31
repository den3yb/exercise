import sys
from multiprocessing import Pool    #cd Desktop\exercise
                                    #python multyp.py 2 3 1 2 3 4 5 6
def summ(m: list) -> int:
    return sum(m)

def main() -> None:

    s=int(sys.argv[1]) #для строг - string
    c=int(sys.argv[2]) #для столбцов -  colums
    mat = []

    for i in range (int(s)):
        m=[]
        for j in range (int(c)):
            m.append(int(sys.argv[i*int(c)+j+3]))
        mat.append(m)

    for i in range (s): #вывод для проверки
        for j in range (c):
            print(mat[i][j], end = " ") 
        print()

    sumt = [] #временная сумма, sum temp, в ней будет список сумм по рядам

    with Pool(s) as p:
        sumt += p.map(summ, mat)

    for i in range (int(s)):
        print(sumt[i])
