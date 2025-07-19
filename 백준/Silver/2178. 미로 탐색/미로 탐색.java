import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int n = Integer.parseInt(tokenizer.nextToken());
        int m = Integer.parseInt(tokenizer.nextToken());

        int[][] board = new int[n][m];
        for (int i = 0; i < n; i++) {
            String line = reader.readLine();
            for (int j = 0; j < m; j++) {
                board[i][j] = Character.getNumericValue(line.charAt(j));
            }
        }

        int[] dx = new int[]{-1, 0, 1, 0};
        int[] dy = new int[]{0, 1, 0, -1};

        Deque<Point> queue = new ArrayDeque<>();
        queue.addLast(new Point(0, 0));

        while (!queue.isEmpty()) {
            Point point = queue.removeFirst();
            if (point.x == n - 1 && point.y == m - 1) {
                System.out.println(board[point.x][point.y]);
                return;
            }

            for (int k = 0; k < 4; k++) {
                int nx = point.x + dx[k];
                int ny = point.y + dy[k];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m &&
                        board[nx][ny] == 1) {
                    queue.addLast(new Point(nx, ny));
                    board[nx][ny] = board[point.x][point.y] + 1;
                }
            }
        }
    }
}

class Point {
    int x;
    int y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
