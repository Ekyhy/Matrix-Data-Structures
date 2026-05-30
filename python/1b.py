# Sort Matrix Column Wise
import numpy as np

def transpose(mat):
    row = len(mat)
    col = len(mat[0])

    tr = [[0 for _ in range (row)] for _ in range(col)]

    for i in range(row):
        for j in range(col):
            tr[j][i] = mat[i][j]
    return tr

def RowWiseSort(B):
    for i in range (len(B)):
        B[i] = sorted(B[i])
    return B

def sortCol(mat,n):
    B = transpose(mat)

    B = RowWiseSort(B)

    mat= transpose(B)

    for i in range(n):
        for j in range(n):
            print(mat[i][j], end = " ")
        print()

if __name__ == '__main__':
    n = int(input(f"Masukkan Ordo Matriks: "))
    vals = list(map(int,input(f"Masukkan elemen matriks {n * n} (dipisah spasi): ").split()))

    mat = []
    idx = 0
    for i in range(n):
        row = []
        for j in range(n):
            row.append(vals[idx])
            idx += 1
        mat.append(row)

    sortCol(mat,n)

