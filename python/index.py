import importlib.util
import os

# Load modules dari file yang ada
def load_module(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    spec = importlib.util.spec_from_file_location(filename[:-3], filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

mod_1a = load_module('sortRows.py')
mod_1b = load_module('sortCol.py')
mod_2a = load_module('rotateMatrixClockwise.py')
mod_2b = load_module('rotateMatrix.py')
mod_2c = load_module('rotateMatrix90.py')
mod_2d = load_module('rotateMatriks180.py')
mod_3a = load_module('row_major.py')
mod_3b = load_module('col_major.py')
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

def deep_copy_matrix(mat):
    """Helper untuk membuat copy matriks"""
    return [row[:] for row in mat]

def menu():
    """Menu utama CLI dengan penyimpanan hasil operasi"""
    print("\n" + "="*60)
    print("         SELAMAT DATANG DI PROGRAM OPERASI MATRIKS")
    print("="*60)
    
    # Input ordo matriks di awal
    while True:
        try:
            n = int(input("\nMasukkan ordo matriks (n x n): "))
            if n <= 0:
                print("Ordo harus lebih besar dari 0!")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
    
    # Input nilai matriks di awal
    print(f"\nMasukkan {n*n} elemen matriks (dipisah dengan spasi):")
    print("Contoh untuk matriks 2x2: 1 2 3 4")
    mat = input_matrix(n)
    
    # Tampilkan matriks awal
    print_matrix(mat, "Matriks Awal:")
    
    history = [deep_copy_matrix(mat)]
    operation_count = 0
    
    # Menu loop utama
    while True:
        print("\n" + "="*60)
        print("            MENU OPERASI MATRIKS")
        print("="*60)
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
        print("11. Reset ke Matriks Awal")
        print("12. Lihat Riwayat Operasi")
        print("13. Exit")
        print("="*60)
        
        choice = input("Pilih menu (1-13): ")
        
        if choice == '13':
            print("\nTerima kasih telah menggunakan program ini!")
            print(f"Total operasi yang dilakukan: {operation_count}")
            break
        
        if choice == '11':
            mat = deep_copy_matrix(history[0])
            print_matrix(mat, "Matriks direset ke kondisi awal:")
            operation_count = 0
            history = [deep_copy_matrix(mat)]
            continue
        
        if choice == '12':
            print(f"\nTotal operasi yang telah dilakukan: {operation_count}")
            print(f"Matriks saat ini: {len(history)} state tersimpan")
            print_matrix(mat, "Matriks Saat Ini:")
            continue
        
        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            print("Input tidak valid! Silakan pilih menu 1-13.")
            continue
        
        # Buat copy untuk hasil operasi
        result_mat = deep_copy_matrix(mat)
        operation_name = ""
        show_result = True
        
        try:
            if choice == '1':
                sortRows(result_mat, n)
                operation_name = "Sort Row-wise"
                print_matrix(result_mat, f"Hasil {operation_name}:")
                
            elif choice == '2':
                sortCol(result_mat, n)
                operation_name = "Sort Column-wise"
                print_matrix(result_mat, f"Hasil {operation_name}:")
                
            elif choice == '3':
                rotateMatrixClockwise(result_mat, n)
                operation_name = "Rotate Clockwise"
                print_matrix(result_mat, f"Hasil {operation_name}:")
                
            elif choice == '4':
                rotateMatrix(result_mat, n)
                operation_name = "Rotate Counter-Clockwise"
                print_matrix(result_mat, f"Hasil {operation_name}:")
                
            elif choice == '5':
                rotateMatrix90(result_mat)
                operation_name = "Rotate 90 Degrees"
                print_matrix(result_mat, f"Hasil {operation_name}:")
                
            elif choice == '6':
                rotateMatriks180(result_mat, n)
                operation_name = "Rotate 180 Degrees"
                print_matrix(result_mat, f"Hasil {operation_name}:")
                
            elif choice == '7':
                operation_name = "Row-wise Traversal"
                print(f"\nHasil {operation_name}:")
                row_major(result_mat)
                show_result = False
                
            elif choice == '8':
                operation_name = "Column-wise Traversal"
                print(f"\nHasil {operation_name}:")
                col_major(result_mat)
                show_result = False
                
            elif choice == '9':
                operation_name = "Spiral Traversal"
                result = spirallyTraverse(result_mat)
                print(f"\nHasil {operation_name}:")
                print(result)
                show_result = False
                
            elif choice == '10':
                transpose(result_mat)
                operation_name = "Transpose"
                print_matrix(result_mat, f"Hasil {operation_name}:")
            
            # Simpan hasil jika operasi mengubah matriks
            if show_result:
                ask_save = input("\nSimpan hasil operasi ini? (y/n): ").lower()
                if ask_save == 'y':
                    mat = result_mat
                    history.append(deep_copy_matrix(mat))
                    operation_count += 1
                    print(f"✓ Hasil {operation_name} disimpan. Matriks diperbarui.")
                else:
                    print("Hasil operasi tidak disimpan.")
            
        except Exception as e:
            print(f"Error pada operasi {operation_name}: {str(e)}")

if __name__ == '__main__':
    menu()
