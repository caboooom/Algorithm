import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        StringBuilder builder = new StringBuilder();

        PriorityQueue<Integer> queue = new PriorityQueue<>(
                (x, y) -> {
                    if (Math.abs(x) == Math.abs(y)) {
                        return Integer.compare(x, y);
                    }
                    return Integer.compare(Math.abs(x), Math.abs(y));
                });
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(reader.readLine());
            if (x == 0) {
                if (queue.isEmpty()) {
                    builder.append(0).append("\n");
                } else {
                    builder.append(queue.remove()).append("\n");
                }
            } else {
                queue.add(x);
            }
        }
        System.out.println(builder);
    }
}
