public class RowMajor {
    public static void rowMajor(int[][] arr) {
        for (int[] row : arr) {
            for (int value : row) {
                System.out.print(value + " ");
            }
        }
        System.out.println();
    }
}
