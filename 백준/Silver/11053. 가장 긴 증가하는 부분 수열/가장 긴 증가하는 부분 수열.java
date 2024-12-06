import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
            int n = Integer.parseInt(reader.readLine());
            String[] sarr = reader.readLine().split(" ");
            int[] dp = new int[n];
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(sarr[i]);
            }

            dp[0] = 1;
            for (int i = 1; i < n; i++) {
                for (int j = i - 1; j >= 0; j--) {
                    if (arr[i] > arr[j] && dp[i] < dp[j] + 1) {
                        dp[i] = dp[j] + 1;
                    }
                }
                if (dp[i] == 0) {
                    dp[i] = 1;
                }
            }
            int answer = 0;
            for (int i = 0; i < n; i++) {
                answer = Math.max(answer, dp[i]);
            }
            System.out.println(answer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}