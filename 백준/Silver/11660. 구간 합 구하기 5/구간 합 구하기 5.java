import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int n = Integer.parseInt(tokenizer.nextToken());
        int m = Integer.parseInt(tokenizer.nextToken());
        int[][] table = new int[n][n];
        for (int i = 0; i < n; i++) {
            tokenizer = new StringTokenizer(reader.readLine());
            table[i][0] = Integer.parseInt(tokenizer.nextToken());
            for (int j = 1; j < n; j++) {
                table[i][j] = Integer.parseInt(tokenizer.nextToken()) + table[i][j-1];
            }
        }

        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int sum = 0;
            tokenizer = new StringTokenizer(reader.readLine());
            int x1 = Integer.parseInt(tokenizer.nextToken());
            int y1 = Integer.parseInt(tokenizer.nextToken());
            int x2 = Integer.parseInt(tokenizer.nextToken());
            int y2 = Integer.parseInt(tokenizer.nextToken());
            for (int j = x1-1; j < x2; j++) {
                if (y1 == 1) {
                    sum += table[j][y2-1];
                } else {
                    sum += (table[j][y2 - 1] - table[j][y1 - 2]);
                }
            }
            builder.append(sum).append("\n");
        }
        System.out.println(builder);
    }
}
