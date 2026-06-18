# Sort Matrix Column Wise
import numpy as np

def sortCol(mat, n):
    """
    Sort matriks secara column-wise (mengurutkan setiap kolom)
    Memodifikasi matriks secara in-place
    """
    # Ekstrak setiap kolom, sort, dan kembalikan ke matriks
    for col in range(n):
        # Ambil semua elemen di kolom ini
        column = [mat[row][col] for row in range(n)]
        # Sort kolom
        column.sort()
        # Masukkan kembali ke matriks
        for row in range(n):
            mat[row][col] = column[row]

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

    print("\nSebelum Sort Column-wise:")
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()
    
    sortCol(mat, n)
    
    print("\nSetelah Sort Column-wise:")
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()

