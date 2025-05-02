import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(tokenizer.nextToken());
        int s = Integer.parseInt(tokenizer.nextToken());

        int[] sumArr = new int[n+1];
        tokenizer = new StringTokenizer(reader.readLine(), " ");
        for (int i = 1; i <= n; i++) {
            sumArr[i] = sumArr[i-1] + Integer.parseInt(tokenizer.nextToken());
        }

        int a = 1;
        int b = 1;
        int answer = n + 1;
        while (b <= n) {
            if (sumArr[b] - sumArr[a-1] < s) {
                ++b;
            } else {
                answer = Math.min(answer, b - a + 1);
                ++a;
            }
        }
        if (answer == n+1) {
            System.out.println(0);
        } else {
            System.out.println(answer);
        }
    }
}
