class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[][] board = new int[n][m];
        for (int i = 0; i < puddles.length; i++) {
            board[puddles[i][1]-1][puddles[i][0]-1] = -1; // -1로 표시
        } // O(n)
        board[0][0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == -1) {
                    continue;
                }
                if (i + 1 < n || j + 1 < m) {
                    if (i + 1 < n && board[i+1][j] >= 0) {
                        board[i+1][j] += board[i][j];
                        board[i+1][j]  %= 1000_000_007;
                    }
                    if (j + 1 < m && board[i][j+1] >= 0) {
                        board[i][j+1] += board[i][j];
                        board[i][j+1]  %= 1000_000_007;
                    }
                }
            }
        } // O(n^2)
        
        
        answer = board[n-1][m-1];
        return answer;
    }
}