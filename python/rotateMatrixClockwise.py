import pandas as np

def rotateMatrixClockwise(mat, n):
    if not len(mat):
        return
    
    top = 0
    bottom = len(mat)-1

    left = 0
    right = len(mat[0])-1

    while left < right and top < bottom:
        prev = mat[top+1][left]

        for i in range(left,right+1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
        top += 1

        for i in range(top,bottom+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev= curr
        right -= 1

        for i in range(right, left-1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
        bottom -= 1

        for i in range(bottom, top-1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
        left += 1

    return mat
if __name__ == '__main__':
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

    rotateMatrixClockwise(mat, n)
    
    print('[\n', end='')
    print("After Rotate Clockwise: ")
    for r in mat:
        print('  [', end='')
        print(', '.join(map(str, r)), end='')
        print(']')
    print(']')