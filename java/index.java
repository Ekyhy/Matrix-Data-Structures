import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class index {
    private static final Scanner scanner = new Scanner(System.in);
    private static int currentOrder = 0;
    private static int[][] initialMatrix;
    private static int[][] currentMatrix;
    private static final List<int[][]> historyMatrices = new ArrayList<>();
    private static final List<String> historyLabels = new ArrayList<>();

    public static void main(String[] args) {
        initializeOrder();
        initializeMatrix();
        menu();
    }

    private static void initializeOrder() {
        while (currentOrder <= 0) {
            System.out.print("Masukkan ordo matriks (n x n): ");
            try {
                currentOrder = Integer.parseInt(scanner.nextLine().trim());
                if (currentOrder <= 0) {
                    System.out.println("Ordo harus berupa bilangan bulat positif.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Input tidak valid. Masukkan angka bulat positif.");
            }
        }
    }

    private static void initializeMatrix() {
        System.out.println("\nMasukkan " + (currentOrder * currentOrder) + " elemen matriks (dipisah spasi): ");
        initialMatrix = inputMatrix(currentOrder);
        currentMatrix = cloneMatrix(initialMatrix);
        historyMatrices.clear();
        historyLabels.clear();
        historyMatrices.add(cloneMatrix(currentMatrix));
        historyLabels.add("Matriks awal");
        System.out.println();
        printMatrix(currentMatrix, "Matriks awal (ordo " + currentOrder + " x " + currentOrder + "):");
    }

    private static int[][] cloneMatrix(int[][] mat) {
        int n = mat.length;
        int[][] clone = new int[n][n];
        for (int i = 0; i < n; i++) {
            System.arraycopy(mat[i], 0, clone[i], 0, n);
        }
        return clone;
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

    private static void printHistory() {
        System.out.println();
        System.out.println("==================================================");
        System.out.println("              RIWAYAT OPERASI MATRIKS");
        System.out.println("==================================================");
        for (int i = 0; i < historyMatrices.size(); i++) {
            printMatrix(historyMatrices.get(i), (i + 1) + ". " + historyLabels.get(i));
        }
        System.out.println("==================================================");
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
            System.out.println("11. Reset Matriks");
            System.out.println("12. Lihat Riwayat Operasi");
            System.out.println("13. Exit");
            System.out.println("==================================================");
            System.out.print("Pilih menu (1-13): ");

            String choice = scanner.nextLine().trim();

            if (choice.equals("13")) {
                System.out.println("Terima kasih! Program selesai.");
                break;
            }

            if (choice.equals("11")) {
                currentMatrix = cloneMatrix(initialMatrix);
                historyMatrices.clear();
                historyLabels.clear();
                historyMatrices.add(cloneMatrix(currentMatrix));
                historyLabels.add("Matriks awal");
                System.out.println("Matriks telah direset ke kondisi awal.");
                printMatrix(currentMatrix, "Matriks saat ini:");
                continue;
            }

            if (choice.equals("12")) {
                printHistory();
                continue;
            }

            if (!Arrays.asList("1", "2", "3", "4", "5", "6", "7", "8", "9", "10").contains(choice)) {
                System.out.println("Input tidak valid!");
                continue;
            }

            System.out.println();
            printMatrix(currentMatrix, "Matriks saat ini (ordo " + currentOrder + " x " + currentOrder + "):");
            int[][] result = null;
            String operationName = null;
            boolean modified = false;

            switch (choice) {
                case "1":
                    result = cloneMatrix(currentMatrix);
                    SortRows.sortRows(result);
                    operationName = "Sort Row-wise";
                    printMatrix(result, "Hasil " + operationName + ":");
                    modified = true;
                    break;
                case "2":
                    result = SortColumns.sortCol(cloneMatrix(currentMatrix));
                    operationName = "Sort Column-wise";
                    printMatrix(result, "Hasil " + operationName + ":");
                    modified = true;
                    break;
                case "3":
                    result = cloneMatrix(currentMatrix);
                    RotateClockwise.rotateMatrixClockwise(result);
                    operationName = "Rotate Clockwise";
                    printMatrix(result, "Hasil " + operationName + ":");
                    modified = true;
                    break;
                case "4":
                    result = cloneMatrix(currentMatrix);
                    RotateCounterClockwise.rotateMatrix(result);
                    operationName = "Rotate Counter-Clockwise";
                    printMatrix(result, "Hasil " + operationName + ":");
                    modified = true;
                    break;
                case "5":
                    result = cloneMatrix(currentMatrix);
                    Rotate90.rotateMatrix90(result);
                    operationName = "Rotate 90 Degrees";
                    printMatrix(result, "Hasil " + operationName + ":");
                    modified = true;
                    break;
                case "6":
                    result = cloneMatrix(currentMatrix);
                    Rotate180.rotateMatriks180(result);
                    operationName = "Rotate 180 Degrees";
                    printMatrix(result, "Hasil " + operationName + ":");
                    modified = true;
                    break;
                case "7":
                    System.out.println();
                    operationName = "Row-wise Traversal";
                    System.out.println("Hasil " + operationName + ":");
                    RowMajor.rowMajor(currentMatrix);
                    break;
                case "8":
                    System.out.println();
                    operationName = "Column-wise Traversal";
                    System.out.println("Hasil " + operationName + ":");
                    ColMajor.colMajor(currentMatrix);
                    break;
                case "9":
                    System.out.println();
                    operationName = "Spiral Traversal";
                    System.out.println("Hasil " + operationName + ":");
                    System.out.println(SpiralTraverse.spirallyTraverse(currentMatrix));
                    break;
                case "10":
                    result = cloneMatrix(currentMatrix);
                    Transpose.transpose(result);
                    operationName = "Transpose";
                    printMatrix(result, "Hasil " + operationName + ":");
                    modified = true;
                    break;
                default:
                    result = null;
            }

            if (modified && operationName != null) {
                currentMatrix = result;
                historyMatrices.add(cloneMatrix(currentMatrix));
                historyLabels.add(operationName);
            }
        }
    }
}

