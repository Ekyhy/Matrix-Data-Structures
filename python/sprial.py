def spirallyTraverse(mat):
    m = len(mat)
    n = len(mat[0])

    res = []
    vis = [[False] * n for _ in range(m)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c = 0, 0
    idx = 0

    for _ in range(m * n):
        res.append(mat[r][c])
        vis[r][c] = True
        newR, newC = r + dr[idx], c + dc[idx]

        if 0 <= newR < m and 0 <= newC < n and not vis[newR][newC]:
            r, c = newR, newC
        else:
            idx = (idx + 1) % 4
            r += dr[idx]
            c += dc[idx]

    return res


if __name__ == "__main__":
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


    res = spirallyTraverse(mat)

    print(" ".join(map(str, res)))