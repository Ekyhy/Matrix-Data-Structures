import importlib.util
import os

# Load modules dari file yang ada
def load_module(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    spec = importlib.util.spec_from_file_location(filename[:-3], filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

mod_1a = load_module('1a.py')
mod_1b = load_module('1b.py')
mod_2a = load_module('2a.py')
mod_2b = load_module('2b.py')
mod_2c = load_module('2c.py')
mod_2d = load_module('2d.py')
mod_3a = load_module('3a.py')
mod_3b = load_module('3b.py')
mod_transpose = load_module('trnspose.py')
mod_spiral = load_module('sprial.py')

# Ambil fungsi yang diperlukan
sortRows = mod_1a.sortRows
sortCol = mod_1b.sortCol
rotateMatrixClockwise = mod_2a.rotateMatrixClockwise
rotateMatrix = mod_2b.rotateMatrix
rotateMatrix90 = mod_2c.rotateMatrix90
rotateMatriks180 = mod_2d.rotateMatriks180
row_major = mod_3a.row_major
col_major = mod_3b.col_major
transpose = mod_transpose.transpose
spirallyTraverse = mod_spiral.spirallyTraverse

def input_matrix(n):
    """Helper untuk input matriks"""
    vals = list(map(int, input(f"Masukkan {n*n} elemen (dipisah spasi): ").split()))
    mat = []
    idx = 0
    for i in range(n):
        row = []
        for j in range(n):
            row.append(vals[idx])
            idx += 1
        mat.append(row)
    return mat

def print_matrix(mat, title="Hasil:"):
    """Helper untuk tampilkan matriks"""
    print(f"\n{title}")
    print('[')
    for row in mat:
        print('  [' + ', '.join(map(str, row)) + ']')
    print(']')

def menu():
    """Menu utama CLI"""
    while True:
        print("\n" + "="*50)
        print("       PROGRAM OPERASI MATRIKS")
        print("="*50)
        print("1.  Sort Row-wise")
        print("2.  Sort Column-wise")
        print("3.  Rotate Clockwise (Layer by Layer)")
        print("4.  Rotate Counter-Clockwise (Layer by Layer)")
        print("5.  Rotate 90 Degrees")
        print("6.  Rotate 180 Degrees")
        print("7.  Row-wise Traversal")
        print("8.  Column-wise Traversal")
        print("9.  Spiral Traversal")
        print("10. Transpose")
        print("11. Exit")
        print("="*50)
        
        choice = input("Pilih menu (1-11): ")
        
        if choice == '11':
            print("Terima kasih! Program selesai.")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            print("Input tidak valid!")
            continue
        
        n = int(input("Masukkan ordo matriks (n x n): "))
        mat = input_matrix(n)
        
        print("\nMatriks awal:")
        print_matrix(mat, "")
        
        if choice == '1':
            sortRows(mat, n)
            print_matrix(mat, "Hasil Sort Row-wise:")
            
        elif choice == '2':
            sortCol(mat, n)
            
        elif choice == '3':
            rotateMatrixClockwise(mat, n)
            print_matrix(mat, "Hasil Rotate Clockwise:")
            
        elif choice == '4':
            rotateMatrix(mat,n)
            print_matrix(mat, "Hasil Rotate Counter-Clockwise:")
            
        elif choice == '5':
            rotateMatrix90(mat)
            print_matrix(mat, "Hasil Rotate 90 Degrees:")
            
        elif choice == '6':
            rotateMatriks180(mat, n)
            print_matrix(mat, "Hasil Rotate 180 Degrees:")
            
        elif choice == '7':
            print("\nHasil Row-wise Traversal:")
            row_major(mat)
            
        elif choice == '8':
            print("\nHasil Column-wise Traversal:")
            col_major(mat)
            
        elif choice == '9':
            result = spirallyTraverse(mat)
            print("\nHasil Spiral Traversal:")
            print(result)
            
        elif choice == '10':
            transpose(mat)
            print_matrix(mat, "Hasil Transpose:")

if __name__ == '__main__':
    menu()
