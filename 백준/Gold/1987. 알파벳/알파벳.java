import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

    static int maxCount;
    static Set<Character> characterSet = new HashSet<>();
    static int[] dx = new int[] {-1, 0, 1, 0};
    static int[] dy = new int[] {0, 1, 0, -1};
    static int r;
    static int c;
    static boolean[][] visited;
    static char[][] board;


    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(reader.readLine(), " ");
        r = Integer.parseInt(stringTokenizer.nextToken());
        c = Integer.parseInt(stringTokenizer.nextToken());
        board = new char[r][c];
        visited = new boolean[r][c];

        for (int i = 0; i < r; i++) {
            char[] input = reader.readLine().toCharArray();
            for (int j = 0; j < c; j++) {
                board[i][j] = input[j];
            }
        }

        visited[0][0] = true;
        characterSet.add(board[0][0]);
        dfs(0,0,1);
        System.out.println(maxCount);
    }

    static void dfs(int x, int y, int count) {
        maxCount = Math.max(maxCount, count);

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
                char curr = board[nx][ny];
                if(!characterSet.contains(curr)) {
                    visited[nx][ny] = true;
                    characterSet.add(curr);
                    dfs(nx, ny, count + 1);
                    visited[nx][ny] = false;
                    characterSet.remove(curr);
                }
            }
        }
    }
}