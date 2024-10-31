import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] firstLine = reader.readLine().split(" ");
        int n = Integer.parseInt(firstLine[0]);
        int m = Integer.parseInt(firstLine[1]);
        int r = Integer.parseInt(firstLine[2]);

        int[] visited = new int[n+1];
        Object[] graph = new Object[n+1];

        for(int i = 1; i < n+1; i++) {
            graph[i] = new LinkedList<Integer>();
        }

        for(int i = 0; i < m; i++) {
            String[] input = reader.readLine().split(" ");
            int u = Integer.parseInt(input[0]);
            int v = Integer.parseInt(input[1]);
            ((LinkedList<Integer>)graph[u]).add(v);
            ((LinkedList<Integer>)graph[v]).add(u);            
        }

            Deque<Integer> queue = new ArrayDeque<>();
            queue.offer(r);
            Arrays.fill(visited, -1);
            int current = 0;
            visited[0] = 0;
            visited[r] = 0;
            while(!queue.isEmpty()) {                
                current = queue.poll();
                for(int neighbor : (LinkedList<Integer>)graph[current]) {
                    if(visited[neighbor] < 0) {
                        visited[neighbor] = visited[current] + 1;
                        queue.offer(neighbor);
                    }
                }
            }
        
        for(int i = 1; i < n+1; i++) {
            System.out.println(visited[i]);
        }
    }

}