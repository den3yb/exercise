from multiprocessing import Pool

s=0
c=0
mat = [0]

def create(_s, _c):
    global s
    global c
    global mat
    s=_s
    c=_c
    _mat = []
    for i in range (s):
        m=[]
        for j in range (c):
            m.append(int(input()))
        _mat.append(m)
    mat=_mat
    return mat

def printf():
    for i in range (s):
        for j in range (c):
            print(mat[i][j], end = " ")
        print()


def parsumm():
    with Pool(s) as p:
        st=[]
        for i in range (s):
            st.append(i)
        print(p.map(summ,st))

def summ(x):
    sumtemp = 0
    for i in range (c):
        sumtemp+=mat[x][i]
    return sumtemp