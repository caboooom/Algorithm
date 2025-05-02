import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(tokenizer.nextToken());
        int m = Integer.parseInt(tokenizer.nextToken());

        int[] arr = new int[n+1];
        int[] sumArr = new int[n+1];
        tokenizer = new StringTokenizer(reader.readLine(), " ");
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(tokenizer.nextToken());
            sumArr[i] = sumArr[i-1] + arr[i];
        }

        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < m; i++) {
            tokenizer = new StringTokenizer(reader.readLine(), " ");
            int a = Integer.parseInt(tokenizer.nextToken());
            int b = Integer.parseInt(tokenizer.nextToken());
            builder.append(sumArr[b] - sumArr[a-1]).append("\n");
        }

        System.out.println(builder);
    }
}
