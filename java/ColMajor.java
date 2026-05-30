public class ColMajor {
    public static void colMajor(int[][] arr) {
        int rows = arr.length;
        int cols = arr[0].length;
        for (int j = 0; j < cols; j++) {
            for (int i = 0; i < rows; i++) {
                System.out.print(arr[i][j] + " ");
            }
        }
        System.out.println();
    }
}
