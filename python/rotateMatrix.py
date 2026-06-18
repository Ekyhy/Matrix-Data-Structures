import numpy as np

def rotateMatrix(mat,n):

    # Fungsi untuk memutar matriks berlawanan dengan arah jarum jam
    m = len(mat)
    n = len(mat[0])
    
    row = 0
    col = 0
    prev = 0
    curr = 0

    # Memutar matriks dalam layer
    while row < m and col < n:
        if row + 1 == m or col + 1 == n:
            break

        # Menyimpan elemen pertama untuk kolom berikutnya
        prev = mat[row][col + 1]

        # Memindahkan elemen ke kolom pertama
        for i in range(row, m):
            curr = mat[i][col]
            mat[i][col] = prev
            prev = curr
        col += 1

        # Memindahkan elemen ke baris terakhir
        for i in range(col, n):
            curr = mat[m - 1][i]
            mat[m - 1][i] = prev
            prev = curr
        m -= 1

        # Memindahkan elemen ke kolom terakhir
        if col < n:
            for i in range(m - 1, row - 1, -1):
                curr = mat[i][n - 1]
                mat[i][n - 1] = prev
                prev = curr
        n -= 1

        # Memindahkan elemen ke baris pertama
        if row < m:
            for i in range(n - 1, col - 1, -1):
                curr = mat[row][i]
                mat[row][i] = prev
                prev = curr
        row += 1

if __name__ == "__main__":
    n = int(input(f"Masukkan Ordo Matriks: "))
    vals = list(map(int,input(f"Masukkan elemen matriks {n * n} (dipisah spasi): ").split()))

    mat = np.array(vals).reshape(n,n)
    print('[\n', end='')
    print("Before Rotate Clockwise:")
    for r in mat:
        print('  [', end='')
        print(', '.join(map(str, r)), end='')
        print(']')
    print(']')

    rotateMatrix(mat, n)
    
    print('[\n', end='')
    print("After Rotate Clockwise: ")
    for r in mat:
        print('  [', end='')
        print(', '.join(map(str, r)), end='')
        print(']')
    print(']')