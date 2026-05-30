import java.util.Arrays;

public class SortColumns {
    public static int[][] sortCol(int[][] mat) {
        int n = mat.length;
        int[][] transposed = transpose(mat);
        for (int[] row : transposed) {
            Arrays.sort(row);
        }
        return transpose(transposed);
    }

    private static int[][] transpose(int[][] mat) {
        int n = mat.length;
        int[][] tr = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                tr[j][i] = mat[i][j];
            }
        }
        return tr;
    }
}
