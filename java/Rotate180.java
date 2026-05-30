import java.util.Arrays;

public class Rotate180 {
    public static void sortRows(int[][] mat) {
        for (int[] row : mat) {
            Arrays.sort(row);
        }
    }
    public static void rotateMatriks180(int[][] mat) {
        
        int n = mat.length;
        for (int i = 0; i < n / 2; i++) {
            for (int j = 0; j < n; j++) {
                int temp = mat[i][j];
                mat[i][j] = mat[n - i - 1][n - j - 1];
                mat[n - i - 1][n - j - 1] = temp;
            }
        }

        // Handle the middle row if the matrix 
        // has odd dimensions
        if (n % 2 != 0) {
            int mid = n / 2;
            for (int j = 0; j < n / 2; j++) {
                int temp = mat[mid][j];
                mat[mid][j] = mat[mid][n - j - 1];
                mat[mid][n - j - 1] = temp;
            }
        }

    }
    //     int n = mat.length;
    //     for (int i = 0; i < n; i++) {
    //         reverseRow(mat[i]);
    //     }
    //     for (int i = 0; i < n / 2; i++) {
    //         int[] temp = mat[i];
    //         mat[i] = mat[n - 1 - i];
    //         mat[n - 1 - i] = temp;
    //     }
    // }

    // private static void reverseRow(int[] row) {
    //     int left = 0;
    //     int right = row.length - 1;
    //     while (left < right) {
    //         int temp = row[left];
    //         row[left] = row[right];
    //         row[right] = temp;
    //         left++;
    //         right--;
    //     }
    // }
}
