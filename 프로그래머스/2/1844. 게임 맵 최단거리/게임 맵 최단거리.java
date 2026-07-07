import java.util.*;
// 도달할 수 있다면 , 도착하기까지 최수 칸 개수 리턴
class Solution {
    public int solution(int[][] maps) {
        int answer = -1; // 도달할 수 없는 경우 -1을 리턴
        
        // 1 <= n, m <= 100 
        // 0은 지날 수 없음, 1은 지날 수 있음
        // 최초 위치는 (0,0)
        // 목표 위치는 (n-1, m-1)
        
        int n = maps.length;
        int m = maps[0].length;
        
        int[] dRow = {-1, 0, 1, 0};
        int[] dCol = {0, 1, 0, -1};
        
        int cRow = 0;
        int cCol = 0;
        
        Deque<Position> queue = new ArrayDeque<>();
        queue.add(new Position(cRow, cCol, 1));
        maps[0][0] = 0; //visited
        
        while (queue.size() > 0) {
            Position cPosition = queue.remove();
            cRow = cPosition.row;
            cCol = cPosition.col;
            if (cRow == n - 1 && cCol == m - 1) {
                return cPosition.dist;
            }
            
            for (int i = 0; i < 4; i++) {
                int nRow = cRow + dRow[i];
                int nCol = cCol + dCol[i];
                if (nRow >= 0 && nRow < n && nCol >= 0 && nCol < m) {
                    if (maps[nRow][nCol] == 1) {
                        Position nPosition = new Position(nRow, nCol, cPosition.dist+1);
                        queue.add(nPosition);
                        maps[nRow][nCol] = 0; // visited
                    }
                }
            }
        }
        
        return answer;
    }
}

class Position {
    int row;
    int col;
    int dist;
    public Position(int row, int col, int dist) {
        this.row = row;
        this.col = col;
        this.dist = dist;
    }
}