from multiprocessing import Pool

mat = [[1, 1, 1],  
      [2, 2, 2],  
      [3, 3, 3]] 

s = 3
c = 3

def f(x):
    sumtemp = 0
    for i in range (c):
        sumtemp+=mat[x][i]
    return sumtemp

if __name__ == '__main__':
    with Pool(s) as p:
        st=[]
        for i in range (s):
            st.append(i)
        print(p.map(f,st))