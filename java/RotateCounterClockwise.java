public class RotateCounterClockwise {
    public static void rotateMatrix(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int row = 0;
        int col = 0;
        int prev;
        int curr;

        while (row < m && col < n) {
            if (row + 1 == m || col + 1 == n) {
                break;
            }
            prev = mat[row][col + 1];

            for (int i = row; i < m; i++) {
                curr = mat[i][col];
                mat[i][col] = prev;
                prev = curr;
            }
            col++;

            for (int i = col; i < n; i++) {
                curr = mat[m - 1][i];
                mat[m - 1][i] = prev;
                prev = curr;
            }
            m--;

            if (col < n) {
                for (int i = m - 1; i >= row; i--) {
                    curr = mat[i][n - 1];
                    mat[i][n - 1] = prev;
                    prev = curr;
                }
            }
            n--;

            if (row < m) {
                for (int i = n - 1; i >= col; i--) {
                    curr = mat[row][i];
                    mat[row][i] = prev;
                    prev = curr;
                }
            }
            row++;
        }
    }
}
