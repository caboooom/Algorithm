import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(reader.readLine());

        for (int t=0; t<T; t++){
            int n = Integer.parseInt(reader.readLine());
            String[] strArr = reader.readLine().split(" ");

            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(strArr[i]);
            }

            int[] dp = new int[arr.length];
            dp[0] = arr[0];
            for(int i=1; i<arr.length; i++){
                dp[i] = Math.max(arr[i]+dp[i-1], arr[i]);
            }
        
            int answer = dp[0];
            for(int i=1; i<arr.length; i++){
                answer = Math.max(answer, dp[i]);
            }

            System.out.println(answer);

        }
    }
}
