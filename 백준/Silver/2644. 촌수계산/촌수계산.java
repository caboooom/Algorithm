import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        String[] target = reader.readLine().split(" ");
        int m = Integer.parseInt(reader.readLine());
        int[][] graph = new int[n+1][n+1];


        for (int i = 0; i < m; i++) {
            String[] input = reader.readLine().split(" ");
            int parent = Integer.parseInt(input[0]);
            int child = Integer.parseInt(input[1]);
            graph[parent][child] = 1;
            graph[child][parent] = 1;
        }

        Deque<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n+1];

        int target1 = Integer.parseInt(target[0]);
        int target2 = Integer.parseInt(target[1]);
        queue.offer(target1);
        visited[target1] = true;
        int answer = 0;
        boolean flag = false;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int s = 0; s < size; s++) {
                int curr = queue.poll();

                if (curr == target2) {
                    flag = true;
                    break;
                }

                for (int i = 1; i <= n; i++) {
                    if (graph[curr][i] == 1 && !visited[i]) {
                        queue.offer(i);
                        visited[i] = true;
                    }
                }
            }
            if (flag) {
                break;
            }
            ++answer;
        }

        if (flag) {
            System.out.println(answer);
        } else {
            System.out.println(-1);
        }
    }
}
