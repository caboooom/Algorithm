import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine(), " ");

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(tokenizer.nextToken());
        }
        Arrays.sort(arr);

        int x = Integer.parseInt(reader.readLine());
        int a = 0;
        int b = n-1;
        int answer = 0;
        while (a < b) {
            int sum = arr[a] + arr[b];
            if (sum == x) {
                ++answer;
                --b;
            } else if (sum > x) {
                --b;
            } else {
                ++a;
            }
        }
        System.out.println(answer);
    }
}
