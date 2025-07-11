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

        int[][] board = new int[n+1][m+1];
        for (int i = 1; i <= n; i++) {
            tokenizer = new StringTokenizer(reader.readLine());
            for (int j = 1; j <= m; j++) {
                board[i][j] = Integer.parseInt(tokenizer.nextToken());
            }
        }

        int[][] visited = new int[n+1][m+1];
        Deque<Point> stack = new ArrayDeque<>();
        int[] dx = new int[] {-1, 0, 1, 0};
        int[] dy = new int[] {0, -1, 0, 1};

        int count = 0;
        int maxSize = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                int size = 0;
                if (visited[i][j] == 0) {
                    visited[i][j] = 1;
                    if (board[i][j] == 1) {
                        stack.addLast(new Point(i, j));
                        ++size;
                        ++count;
                        while (!stack.isEmpty()) {
                            Point curr = stack.removeLast();
                            for (int k = 0; k < 4; k++) {
                                int nx = curr.x + dx[k];
                                int ny = curr.y + dy[k];
                                if (nx > 0 && nx <= n && ny > 0 && ny <= m && visited[nx][ny] == 0) {
                                    visited[nx][ny] = 1;
                                    if (board[nx][ny] == 1) {
                                        ++size;
                                        stack.addLast(new Point(nx, ny));
                                    }
                                }

                            }
                        }
                    }
                }
                maxSize = Math.max(maxSize, size);
            }
        }
        System.out.println(count);
        System.out.println(maxSize);
    }
}

class Point {
    int x;
    int y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public boolean equals(Object other) {
        if (other instanceof Point) {
            Point o = (Point)other;
            return this.x == o.x && this.y == o.y;
        }
        return false;
    }
}