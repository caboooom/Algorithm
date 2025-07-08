import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());

        int n = Integer.parseInt(tokenizer.nextToken());
        int m = Integer.parseInt(tokenizer.nextToken());
        int[][] board = new int[n+1][n+1];
        for (int i = 0; i < m; i++) {
            tokenizer = new StringTokenizer(reader.readLine());
            int u = Integer.parseInt(tokenizer.nextToken());
            int v = Integer.parseInt(tokenizer.nextToken());
            board[u][v] = 1;
            board[v][u] = 1;
        }

        int answer = 0;
        int[] visited = new int[n+1];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) {
            if (visited[i] == 1) {
                continue;
            }
            stack.add(i);
            visited[i] = 1;
            while (!stack.isEmpty()) {
                int curr = stack.removeFirst();
                for (int j = 1; j <= n; j++) {
                    if (board[curr][j] == 1 && visited[j] == 0) {
                        visited[j] = 1;
                        stack.addLast(j);
                    }
                }
            }
            ++answer;
        }
        System.out.println(answer);
    }
}
