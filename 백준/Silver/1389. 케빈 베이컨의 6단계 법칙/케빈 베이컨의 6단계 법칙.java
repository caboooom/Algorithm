import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine(), " ");
        int n = Integer.parseInt(tokenizer.nextToken());
        int m = Integer.parseInt(tokenizer.nextToken());

        int[][] distance = new int[n + 1][n + 1];
        int[][] graph = new int[n + 1][n + 1];

        for (int i = 0; i < m; i++) {
            String line = reader.readLine();
            int user1 = Integer.parseInt(line.split(" ")[0]);
            int user2 = Integer.parseInt(line.split(" ")[1]);
            graph[user1][user2] = 1;
            graph[user2][user1] = 1;
        }

        for (int i = 1; i <= n; i++) {
            Deque<Integer> queue = new ArrayDeque<>();
            queue.add(i);
            while (!queue.isEmpty()) {
                int current = queue.removeFirst();
                for (int j = 1; j <= n; j++) {
                    if (j != i && graph[current][j] == 1 && distance[i][j] == 0) {
                        queue.add(j);
                        distance[i][j] = distance[i][current] + 1;
                    }
                }
            }
        }

        int minValue = Integer.MAX_VALUE;
        int answer = 1;
        for (int i = 1; i <= n; i++) {
            int sum = 0;
            for (int j = 1; j <= n; j++) {
                sum += distance[i][j];
            }
            if (sum < minValue) {
                minValue = sum;
                answer = i;
            }
        }
        System.out.println(answer);
    }
}
