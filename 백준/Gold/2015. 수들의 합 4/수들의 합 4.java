import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(tokenizer.nextToken());
        int k = Integer.parseInt(tokenizer.nextToken());

        long answer = 0;
        long sum = 0;
        Map<Long, Integer> count = new HashMap<>();
        tokenizer = new StringTokenizer(reader.readLine(), " ");
        for (int i = 0; i < n; i++) {
            sum += Integer.parseInt(tokenizer.nextToken());
            long diff = sum - k;
            if (count.containsKey(diff)) {
                answer += count.get(diff);
            }
            if (sum == k) {
                ++answer;
            }

            if (count.containsKey(sum)) {
                count.put(sum, count.get(sum) + 1);
            } else {
                count.put(sum, 1);
            }
        }
        System.out.println(answer);
    }
}
