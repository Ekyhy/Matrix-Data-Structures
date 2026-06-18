# Rotate Matrix by 90
import numpy as np

def rotateMatrix90(mat):
    n = len(mat)
    for row in mat:
        row.reverse()
        
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    


if __name__ == '__main__':
    n = int(input(f"Masukkan Ordo Matriks: "))
    vals = list(map(int, input(f"Masukkan elemen matriks {n * n} (dipisah spasi): ").split()))

    mat = []
    idx = 0
    for i in range(n):
        row = []
        for j in range(n):
            row.append(vals[idx])
            idx += 1
        mat.append(row)

    print('[\n', end='')
    print("Before Rotate 90: ")
    for r in mat:
        print('  [', end='')
        print(', '.join(map(str, r)), end='')
        print(']')
    print(']')

    rotateMatrix90(mat)

    print('[\n', end='')
    print("After Rotate 90: ")
    for r in mat:
        print('  [', end='')
        print(', '.join(map(str, r)), end='')
        print(']')
    print(']')