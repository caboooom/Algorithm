import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine(), " ");
        int[] sumArr = new int[n+1];
        for (int i = 1; i <= n; i++) {
            sumArr[i] = sumArr[i-1] + Integer.parseInt(tokenizer.nextToken());
        }

        StringBuilder builder = new StringBuilder();
        int m = Integer.parseInt(reader.readLine());
        for (int i = 0; i < m; i++) {
            tokenizer = new StringTokenizer(reader.readLine(), " ");
            int a = Integer.parseInt(tokenizer.nextToken());
            int b = Integer.parseInt(tokenizer.nextToken());
            builder.append(sumArr[b] - sumArr[a-1]).append("\n");
        }
        System.out.println(builder);
    }
}