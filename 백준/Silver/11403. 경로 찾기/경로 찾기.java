import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        
        int[][] graph = new int[n][n];

        for(int i = 0; i < n; i++) {
            String[] line = reader.readLine().split(" ");
            for(int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(line[j]);
            }
        }
        
        for(int i = 0; i < n; i++) {
            StringBuilder builder = new StringBuilder();
            for(int target = 0; target < n; target++) {
                
                boolean flag = true;
                if(i == target) {
                    flag = false;
                }
                Deque<Integer> q = new ArrayDeque<>();
                int[] visited = new int[n];
                q.offer(i);
                int hasRoute = 0;
                while(!q.isEmpty()) {
                    int current = q.poll();
                    visited[current] = 1;
                    if(current == target && flag) {
                        hasRoute = 1;
                        break;
                    }
                    for(int j = 0; j < n; j++) {
                        if (graph[current][j] == 1 &&(j == target || visited[j] == 0)) {
                            q.offer(j);
                        }
                    }
                    flag = true;
                }
                builder.append(hasRoute).append(" ");
            }
            System.out.println(builder);
        }
    }
    
}
