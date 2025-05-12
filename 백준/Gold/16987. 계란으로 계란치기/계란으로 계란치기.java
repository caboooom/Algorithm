import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int maxBroken;
    static int n;
    static int[][] eggs;

    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(reader.readLine());
        eggs = new int[n][2];

        for (int i = 0; i < n; i++) {
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine(), " ");
            eggs[i][0] = Integer.parseInt(tokenizer.nextToken());
            eggs[i][1] = Integer.parseInt(tokenizer.nextToken());
        }

        dfs(0);

        System.out.println(maxBroken);
    }

    static void dfs(int idx) {
        if (idx == n) {
         int broken = 0;
         for (int i = 0; i < n; i++) {
             if (eggs[i][0] <= 0) {
                 broken++;
             }
         }
            maxBroken = Math.max(maxBroken, broken);
            return;
        }
        if (eggs[idx][0] <= 0) {
            dfs(idx+1);
            return;
        }
        boolean hit = false;
        for (int i = 0; i < n; i++) {
            if (i == idx || eggs[i][0] <= 0) {
                continue;
            }
            hit = true;
            eggs[idx][0] -= eggs[i][1];
            eggs[i][0] -= eggs[idx][1];
            dfs(idx+1);

            // 원상복구
            eggs[idx][0] += eggs[i][1];
            eggs[i][0] += eggs[idx][1];
        }
        if (!hit) {
            dfs(idx+1);
        }
    }
}
