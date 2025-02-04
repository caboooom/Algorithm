import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] input = reader.readLine().split(" ");
        long a = Long.parseLong(input[0]);
        long b = Long.parseLong(input[1]);

        Deque<Long> queue = new LinkedList<>();
        queue.offer(a);

        long depth = 0;
        while(!queue.isEmpty()) {
            ++depth;
            long size = queue.size();
            for (long i = 0; i < size; i++) {
                long curr = queue.poll();
                if (curr == b) {
                    System.out.println(depth);
                    return;
                }
                long n1 = curr * 2;
                long n2 = curr * 10 + 1;
                if (n1 <= b) {
                    queue.offer(n1);
                }
                if (n2 <= b) {
                    queue.offer(n2);
                }
            }
        }
        System.out.println(-1);

    }
}
