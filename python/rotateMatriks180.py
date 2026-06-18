# Rotate Matix by 180
def rotateMatriks180(mat,n):
# Sort data perbaris
    for row in mat:
        row.sort()
# 
    n = len(mat)
    for i in range(n):
        mat[i].reverse()
    
    mat.reverse()

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
    print("Before Rotate 180: ")
    for r in mat:
        print('  [', end='')
        print(', '.join(map(str, r)), end='')
        print(']')
    print(']')

    rotateMatriks180(mat,n)

    print('[\n', end='')
    print("After Rotate 180: ")
    for r in mat:
        print('  [', end='')
        print(', '.join(map(str, r)), end='')
        print(']')
    print(']')