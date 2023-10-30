from multiprocessing import Pool
from matrix import *

if __name__ == '__main__':
    s=int(input("Ваедите число строк"))
    c=int(input("Ваедите число столбцов"))
    m=create(s, c)
    printf()
    parsumm()