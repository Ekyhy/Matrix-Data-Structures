import numpy as np
def sortRows(mat, n):
    for row in mat:
        row.sort()


if __name__ == '__main__':
    n = int(input(f"Masukkan ordo matriks: "))
    print("Masukkan nilai angka: ")
    vals = list(map(int,input().split()))
    mat = np.array(vals).reshape(n, n)
    sortRows(mat, n)

    print('[\n', end='')
    for row in mat:
        print('  [', end='')
        print(', '.join(map(str, row)), end='')
        print(']')
    print(']')