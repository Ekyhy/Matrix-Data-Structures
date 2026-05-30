import java.util.Arrays;

public class SortRows {
    public static void sortRows(int[][] mat) {
        for (int[] row : mat) {
            Arrays.sort(row);
        }
    }
}
