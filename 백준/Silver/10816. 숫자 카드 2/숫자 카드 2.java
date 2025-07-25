
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        Map<Integer, Integer> numbers = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(tokenizer.nextToken());
            if (numbers.containsKey(num)) {
                numbers.put(num, numbers.get(num) + 1);
            } else {
                numbers.put(num, 1);
            }
        }

        int m = Integer.parseInt(reader.readLine());
        tokenizer = new StringTokenizer(reader.readLine());
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int num = Integer.parseInt(tokenizer.nextToken());
            if (numbers.containsKey(num)) {
                builder.append(numbers.get(num));
            } else {
                builder.append("0");
            }
            builder.append(" ");
        }

        System.out.println(builder);
    }
}
