import java.util.ArrayList;
import java.util.List;

public class SpiralTraverse {
    public static List<Integer> spirallyTraverse(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        List<Integer> res = new ArrayList<>();
        boolean[][] vis = new boolean[m][n];
        int[] dr = {0, 1, 0, -1};
        int[] dc = {1, 0, -1, 0};
        int r = 0;
        int c = 0;
        int idx = 0;

        for (int step = 0; step < m * n; step++) {
            res.add(mat[r][c]);
            vis[r][c] = true;
            int newR = r + dr[idx];
            int newC = c + dc[idx];
            if (newR >= 0 && newR < m && newC >= 0 && newC < n && !vis[newR][newC]) {
                r = newR;
                c = newC;
            } else {
                idx = (idx + 1) % 4;
                r += dr[idx];
                c += dc[idx];
            }
        }
        return res;
    }
}
