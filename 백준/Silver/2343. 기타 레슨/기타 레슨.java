
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int n = Integer.parseInt(tokenizer.nextToken());
        int m = Integer.parseInt(tokenizer.nextToken());
        int[] lessons = new int[n];
        tokenizer = new StringTokenizer(reader.readLine());

        int max = 0;
        long total = 0;

        for (int i = 0; i < n; i++) {
            lessons[i] = Integer.parseInt(tokenizer.nextToken());
            total += lessons[i];
            max = Math.max(max, lessons[i]); 
        }

        long left = max;
        long right = total;
        long answer = 0;

        while (left <= right) {
            long mid = (left + right) / 2;
            int count = 1;
            long sum = 0;

            for (int i = 0; i < n; i++) {
                if (sum + lessons[i] > mid) {
                    count++;
                    sum = lessons[i];
                } else {
                    sum += lessons[i];
                }
            }

            if (count <= m) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        System.out.println(answer);
    }
}
