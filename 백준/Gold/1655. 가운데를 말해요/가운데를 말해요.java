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

        PriorityQueue<Integer> leftQueue = new PriorityQueue<>(
                Comparator.reverseOrder()
        );
        PriorityQueue<Integer> rightQueue = new PriorityQueue<>(

        );
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(reader.readLine());

            if (leftQueue.isEmpty() || leftQueue.peek() > x) {
                leftQueue.add(x);
            } else {
                rightQueue.add(x);
            }

            if (leftQueue.size() > rightQueue.size() + 1) {
                rightQueue.add(leftQueue.poll());
            } else if (leftQueue.size() < rightQueue.size()) {
                leftQueue.add(rightQueue.poll());
            }

            builder.append(leftQueue.peek()).append("\n");
        }
        System.out.println(builder);
    }
}
