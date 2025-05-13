import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static Set<Character> characterSet = new HashSet<>();
    static int maxCount = 0;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static char[][] board;
    static int c;
    static int r;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine(), " ");
        r = Integer.parseInt(tokenizer.nextToken());
        c = Integer.parseInt(tokenizer.nextToken());
        board = new char[r][c];
        visited = new boolean[r][c];
        for (int i = 0; i < r; i++) {
            char[] input = reader.readLine().toCharArray();
            for (int j = 0; j < c; j++) {
                board[i][j] = input[j];
            }
        }
        characterSet.add(board[0][0]);
        visited[0][0] = true;
        dfs(0,0,1);
        System.out.println(maxCount);
    }

    static void dfs(int x, int y, int count) {
        maxCount = Math.max(count, maxCount);
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
                char curr = board[nx][ny];
                if (!characterSet.contains(curr)) {
                    visited[nx][ny] = true;
                    characterSet.add(board[nx][ny]);
                    dfs(nx, ny, count+1);
                    // 다시 복구하기
                    visited[nx][ny] = false;
                    characterSet.remove(board[nx][ny]);
                }
            }
        }
    }
}

