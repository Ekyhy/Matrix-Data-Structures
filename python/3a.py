def row_major(arr):
    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end=" ")
    print()

if __name__ == '__main__':
    n = int(input("Masukkan Ordo Matriks: "))
    vals = list(map(int, input(f"Masukkan {n*n} elemen (dipisah spasi): ").split()))
    
    # Bangun matriks
    arr = []
    idx = 0
    for i in range(n):
        row = []
        for j in range(n):
            row.append(vals[idx])
            idx += 1
        arr.append(row)

    print('[\n', end='')
    print("Before row-major: ")
    for r in arr:
        print('  [', end='')
        print(', '.join(map(str, r)), end='')
        print(']')
    print(']')
    
    print("After row-major :")
    row_major(arr)
