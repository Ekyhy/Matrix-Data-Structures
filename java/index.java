import java.util.Arrays;
import java.util.Scanner;

public class index {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        menu();
    }

    private static int[][] inputMatrix(int n) {
        System.out.print("Masukkan " + (n * n) + " elemen (dipisah spasi): ");
        String[] tokens = scanner.nextLine().trim().split("\\s+");
        int[][] mat = new int[n][n];
        int idx = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                mat[i][j] = Integer.parseInt(tokens[idx++]);
            }
        }
        return mat;
    }

    private static void printMatrix(int[][] mat, String title) {
        System.out.println();
        if (title != null && !title.isEmpty()) {
            System.out.println(title);
        }
        System.out.println("[");
        for (int[] row : mat) {
            System.out.print("  [");
            for (int j = 0; j < row.length; j++) {
                System.out.print(row[j]);
                if (j < row.length - 1) {
                    System.out.print(", ");
                }
            }
            System.out.println("]");
        }
        System.out.println("]");
    }

    private static void menu() {
        while (true) {
            System.out.println();
            System.out.println("==================================================");
            System.out.println("       PROGRAM OPERASI MATRIKS");
            System.out.println("==================================================");
            System.out.println("1.  Sort Row-wise");
            System.out.println("2.  Sort Column-wise");
            System.out.println("3.  Rotate Clockwise (Layer by Layer)");
            System.out.println("4.  Rotate Counter-Clockwise (Layer by Layer)");
            System.out.println("5.  Rotate 90 Degrees");
            System.out.println("6.  Rotate 180 Degrees"); 
            System.out.println("7.  Row-wise Traversal");
            System.out.println("8.  Column-wise Traversal");
            System.out.println("9.  Spiral Traversal");
            System.out.println("10. Transpose");
            System.out.println("11. Exit");
            System.out.println("==================================================");
            System.out.print("Pilih menu (1-11): ");

            String choice = scanner.nextLine().trim();

            if (choice.equals("11")) {
                System.out.println("Terima kasih! Program selesai.");
                break;
            }

            if (!Arrays.asList("1", "2", "3", "4", "5", "6", "7", "8", "9", "10").contains(choice)) {
                System.out.println("Input tidak valid!");
                continue;
            }

            System.out.print("Masukkan ordo matriks (n x n): ");
            int n = Integer.parseInt(scanner.nextLine().trim());
            int[][] mat = inputMatrix(n);

            System.out.println();
            System.out.println("Matriks awal:");
            printMatrix(mat, "");

            switch (choice) {
                case "1":
                    SortRows.sortRows(mat);
                    printMatrix(mat, "Hasil Sort Row-wise:");
                    break;
                case "2":
                    int[][] sortedCols = SortColumns.sortCol(mat);
                    printMatrix(sortedCols, "Hasil Sort Column-wise:");
                    break;
                case "3":
                    RotateClockwise.rotateMatrixClockwise(mat);
                    printMatrix(mat, "Hasil Rotate Clockwise:");
                    break;
                case "4":
                    RotateCounterClockwise.rotateMatrix(mat);
                    printMatrix(mat, "Hasil Rotate Counter-Clockwise:");
                    break;
                case "5":
                    Rotate90.rotateMatrix90(mat);
                    printMatrix(mat, "Hasil Rotate 90 Degrees:");
                    break;
                case "6":
                    Rotate180.rotateMatriks180(mat);
                    printMatrix(mat, "Hasil Rotate 180 Degrees:");
                    break;
                case "7":
                    System.out.println();
                    System.out.println("Hasil Row-wise Traversal:");
                    RowMajor.rowMajor(mat);
                    break;
                case "8":
                    System.out.println();
                    System.out.println("Hasil Column-wise Traversal:");
                    ColMajor.colMajor(mat);
                    break;
                case "9":
                    System.out.println();
                    System.out.println("Hasil Spiral Traversal:");
                    System.out.println(SpiralTraverse.spirallyTraverse(mat));
                    break;
                case "10":
                    Transpose.transpose(mat);
                    printMatrix(mat, "Hasil Transpose:");
                    break;
            }
        }
    }
}

