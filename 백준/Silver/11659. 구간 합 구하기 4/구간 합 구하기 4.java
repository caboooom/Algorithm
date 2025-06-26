import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int n = Integer.parseInt(tokenizer.nextToken());
        int m = Integer.parseInt(tokenizer.nextToken());
        tokenizer = new StringTokenizer(reader.readLine());
        int[] sum = new int[n + 1];
        sum[1] = Integer.parseInt(tokenizer.nextToken());
        for (int i = 2; i <= n; i++) {
            sum[i] = sum[i-1] + Integer.parseInt(tokenizer.nextToken());
        }

        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < m; i++) {
            tokenizer = new StringTokenizer(reader.readLine());
            int start = Integer.parseInt(tokenizer.nextToken());
            int end = Integer.parseInt(tokenizer.nextToken());
            builder.append(sum[end] - sum[start - 1]).append("\n");
        }
        System.out.println(builder);
    }
}
