import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        int answer = 0;

        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (int i = 0; i < n ; i++) {
            queue.add(Integer.parseInt(reader.readLine()));
        }

        while (queue.size() >= 2) {
            int a = queue.poll();
            int b = queue.poll();
            int sum = a + b;
            queue.add(sum);
            answer += sum;
        }
        System.out.println(answer);
    }
}
